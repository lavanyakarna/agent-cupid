# Submission text (draft)

## Overall explanation — 178 characters

> Agent Cupid prototypes a playful dating-agent UI with 25 candidate public-profile records, simulated dates, and ranked cards. It does not infer real preferences or send messages.

Character count includes spaces and punctuation: **178 / 200**.

## Technical section: scraping and analysis stack

### Current implementation

The frontend is a single-page HTML/CSS/JavaScript app. The API is Python + FastAPI. The 25 demo records are loaded from `backend/verified_profiles.json`; the app currently performs **no scraping and no AI profile analysis**. The API has read-only routes only. Date logs and match scores are seeded demo output, not findings about the people listed.

### Proposed consent-based ingestion stack

1. **Consent and URL validation:** accept links only after the submitting person confirms they are their own profiles and grants permission. Validate HTTPS and allow only the intended LinkedIn/Instagram domains. Store a consent timestamp and offer deletion.
2. **Data access:** prefer official, authorized APIs or a profile export supplied by the user. Use `httpx` plus `BeautifulSoup` only for pages that are openly accessible and whose platform terms and robots rules permit automated access. Do not automate logged-in sessions, evade CAPTCHAs, bypass access controls, or scrape private content. Platform restrictions can mean a profile URL alone is not enough to retrieve usable data.
3. **Normalization:** validate extracted fields with Pydantic; retain only minimal, source-linked public facts and explicitly stated interests. Keep the source URL beside each fact and set a retention/deletion policy.
4. **Agent and ranking layer:** generate structured summaries and match explanations from those explicit facts only. Show the basis for every ranking; avoid claims about private dating preferences, personality, sensitive traits, or real-world compatibility. Simulated dates must be labeled as simulations and must never send messages.
5. **Deployment:** FastAPI is the planned backend and Vercel the planned host. This snapshot has no Vercel deployment configuration. See [Vercel's FastAPI deployment guide](https://vercel.com/docs/frameworks/backend/fastapi).

**Disclosure:** Steps 1–5 are a proposed implementation plan, not features currently present in this prototype. Do not submit this section as an implemented scraper description until the consent-based ingestion and analysis code exists and has been tested.
