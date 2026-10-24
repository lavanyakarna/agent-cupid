# YouTube demo script — target runtime 2:45

**Status: recording draft only.** The current code does not yet accept profile submissions or implement `/analyze`; its date logs and rankings are placeholders. Do not record the sections marked **BLOCKED** as if they work. Finish and test those features first.

## Pre-record checklist

- [ ] A consenting test user can submit their own LinkedIn and Instagram links.
- [ ] The analysis screen shows only source-backed facts and links, and clearly labels limitations.
- [ ] Agent conversations are visibly simulated; no messages are sent.
- [ ] Rankings vary for explainable, data-backed reasons—not because of list order or a uniform score.
- [ ] The 25 public-profile records remain marked **demo only** and are never presented as participants.
- [ ] Record the website and browser, not a mockup; hide personal credentials and private data.

## Timed script and screen directions

### 0:00–0:15 — Introduce the project
**On screen:** Open the landing/People screen; show the Agent Cupid title.

**Narration:** “This is Agent Cupid, a prototype for consent-based introductions between AI agents. It uses only information a user chooses to share, and every conversation shown here is a simulation—not a message to a real person.”

### 0:15–0:40 — Submit profile links **[BLOCKED until implemented]**
**On screen:** Use a consenting test account. Enter its own LinkedIn and Instagram links; show the consent checkbox and submit action.

**Narration:** “I’m sharing my own profile links and granting permission for this demo. The app validates the links before attempting any permitted data access.”

### 0:40–1:10 — Show profile analysis **[BLOCKED until implemented]**
**On screen:** Show extracted topics with a visible source link beside each one. Point out any unavailable fields rather than guessing.

**Narration:** “The analysis summarizes public facts that can be traced back to their sources. It does not guess private dating preferences or sensitive traits. If a platform blocks access, the app says so instead of inventing a profile.”

### 1:10–1:45 — Show the agent date
**On screen:** Open the Dates screen and play one clearly labeled simulated conversation based on explicit, source-backed topics.

**Narration:** “Here the agents compare a few shared topics in a simulated date. No one is contacted, and this is not evidence that any public-profile demo person participated.”

### 1:45–2:15 — Show rankings
**On screen:** Open Matches. Select the test user and show a ranked list with a short reason and source-backed factors for each result.

**Narration:** “The ranking is an explainable demo score, not a claim of real-world romantic compatibility. Each result shows which stated topics contributed, so the user can understand and challenge it.”

### 2:15–2:35 — Explain the stack
**On screen:** Briefly show the repository structure or README.

**Narration:** “The interface uses HTML, CSS, and JavaScript. The API is Python with FastAPI. Profile ingestion uses consented, permitted sources; the demo data is stored separately and labeled clearly.”

### 2:35–2:45 — Close
**On screen:** Return to the website and display the demo-only / no-messages notice.

**Narration:** “That’s Agent Cupid: a transparent prototype for agent-mediated introductions, built to keep consent and clear explanations first.”
