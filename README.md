# Agent Cupid - prototype

A playful frontend and FastAPI seed API for exploring an agent-mediated dating concept.

> **Important status note:** This snapshot is a prototype, not a complete dating or profile-analysis product. It includes 25 candidate public-profile records for a demo. No consent or participation is implied; the app does not infer real dating preferences and must not contact anyone.

## What is currently implemented

- Animated single-page frontend with People, Agent Dates, Matches, and Me screens.
- FastAPI read-only routes for health, people, dates, and rankings.
- A JSON seed file containing 25 candidate public-profile records and evidence links.
- Demo date logs and ranking cards.

## What is not implemented yet

- A form or API route for submitting a user's own LinkedIn/Instagram links.
- A `/analyze` endpoint or a profile scraper.
- Evidence-backed profile analysis or personalized compatibility. Seed interests and hobbies are empty; every profile has the same demo vibe, so the current score is a uniform **75%** placeholder.
- A real-time agent-to-agent conversation. The date logs are generated demo text, and pairs are formed by adjacent seed-list order.
- Production Vercel configuration, public GitHub publication, or the required recorded YouTube demo.

Do not describe the current scores, logs, or seed URLs as real romantic compatibility or as proof that any listed person participates.

## Local setup (Windows PowerShell)

### 1. Start the FastAPI backend

From the repository root:

```powershell
cd .\backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Keep this terminal open.

### 2. Serve the frontend

Open a second PowerShell terminal at the repository root:

```powershell
py -m http.server 5500 --directory frontend
```

Open <http://127.0.0.1:5500>. On localhost, the frontend requests the API at `http://127.0.0.1:8000`.

## Current API

- `GET /health`
- `GET /people`
- `GET /people/{person_id}`
- `GET /dates`
- `GET /rankings`
- `GET /rankings/{person_id}`

There are no POST routes in this snapshot.

## Data notes

`backend/verified_profiles.json` contains public-profile candidates, evidence URLs, verification labels, and demo-only notices. Verification confidence varies. The presence of a URL is not proof of ownership, consent, or participation; review entries before redistributing the dataset.

## Privacy and production requirements

Before enabling real analysis, require explicit consent from the person whose profile is submitted, use authorized APIs or user-provided exports where possible, minimize retained data, provide deletion, and show evidence for any extracted public facts. Never bypass login, access controls, or rate limits. Do not infer sensitive traits or private dating preferences from public profiles. Keep the 25-person set labeled as demo-only and do not send messages.

CORS currently allows every origin for local prototyping. Restrict it before production deployment. Vercel deployment is not configured in this snapshot.
