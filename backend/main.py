from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI(title="Agent Cupid API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- SEED DATA (25 candidate profiles) ----------------
PROFILE_FILE = Path(__file__).resolve().with_name("verified_profiles.json")
with PROFILE_FILE.open(encoding="utf-8") as profile_file:
    PROFILE_RECORDS = json.load(profile_file)

PEOPLE = [
    {
        "id": profile["id"],
        "name": profile["name"],
        "role": "Public-profile demo",
        "vibe": "Public-profile demo",
        "color": ["#FF4D8D", "#9B7BFF", "#FFC93C", "#3DDBB0"][i % 4],
        "linkedin": profile["linkedin"],
        "instagram": profile["instagram"],
        "accessory": "",
        "agent": "Demo only: no consent or participation is implied; personal dating preferences are not inferred, and no messages are sent.",
        "needs": [],
        "hobbies": [],
        "interests": [],
        "qualities": ["No personal traits inferred"],
    }
    for i, profile in enumerate(PROFILE_RECORDS)
]

# ---------------- HELPERS ----------------
def compatibility(a, b):
    score = 50
    if a["vibe"] == b["vibe"]:
        score += 25
    shared_interests = set(a["interests"]) & set(b["interests"])
    score += len(shared_interests) * 6
    shared_hobbies = set(a["hobbies"]) & set(b["hobbies"])
    score += len(shared_hobbies) * 4
    return min(score, 98)


def make_dates():
    dates = []
    n = len(PEOPLE)
    for i in range(0, n, 2):
        if i + 1 < n:
            a = PEOPLE[i]
            b = PEOPLE[i + 1]
            score = compatibility(a, b)
            dates.append(
                {
                    "id": len(dates) + 1,
                    "agent_a": a["name"],
                    "agent_b": b["name"],
                    "score": score,
                    "status": "complete",
                    "log": (
                        f"{a['name']}'s agent and {b['name']}'s agent met for coffee. "
                        "They bonded over "
                        f"{', '.join(set(a['interests']) & set(b['interests']) or ['mutual interests'])}. "
                        f"Compatibility: {score}%."
                    ),
                    "image_a": a["accessory"],
                    "image_b": b["accessory"],
                }
            )
    return dates


DATES = make_dates()


def make_rankings():
    rankings = {}
    for person in PEOPLE:
        others = [p for p in PEOPLE if p["id"] != person["id"]]
        scored = []
        for other in others:
            score = compatibility(person, other)
            shared = list(set(person["interests"]) & set(other["interests"]))
            reason = f"Both love {shared[0]}." if shared else "Great vibe match."
            scored.append({"person": other, "score": score, "reason": reason})
        scored.sort(key=lambda x: x["score"], reverse=True)
        rankings[person["id"]] = scored[:5]
    return rankings


RANKINGS = make_rankings()

# ---------------- API ROUTES ----------------
@app.get("/")
def root():
    return {"message": "Agent Cupid API is running 💘"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/people")
def get_people():
    return PEOPLE


@app.get("/people/{person_id}")
def get_person(person_id: int):
    for person in PEOPLE:
        if person["id"] == person_id:
            return person
    return {"error": "Person not found"}


@app.get("/dates")
def get_dates():
    return DATES


@app.get("/rankings")
def get_rankings():
    return RANKINGS


@app.get("/rankings/{person_id}")
def get_person_rankings(person_id: int):
    return RANKINGS.get(person_id, [])
