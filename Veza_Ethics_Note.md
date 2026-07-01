# Veza — Ethics & Data-Handling Note

*Submitted as ethics documentation for the Africa AI Safety Prize Competition 2026.*

## Nature of the data
Veza collects voluntary reports of scam experiences via WhatsApp. Reports contain the type of harm, the channel, the impact, whether it was reported before, and optional free text, voice notes, or screenshots. No formal ethics-board approval was obtained for this prototype; the measures below were applied to manage the ethical risks of collecting sensitive experiences from potentially vulnerable people.

## Who could be affected
Reporters are members of the public who have recently experienced or witnessed a scam. Some may be distressed, may have lost money, and may include elderly or low-digital-literacy users — groups disproportionately targeted by AI-enabled fraud.

## Data minimisation
- **Phone numbers from reports are stripped before storage and never saved.** Each report is stored against a random ID only. Users are told this in the first message they receive.
- Demographic questions are optional.
- Only reports completing all questions are stored; partial sessions are discarded.

## Consent
- Participation is fully voluntary; users initiate the conversation.
- The free-text, voice-note, and screenshot steps are clearly optional (users can reply SKIP).
- The weekly digest is opt-in. Only if a user opts in is their number stored, in a separate list, and it is deleted immediately on STOP/unsubscribe.

## Reducing harm to reporters
- Questions are short and framed around helping others, to reduce shame.
- No follow-up is ever requested.
- Every reporter receives concrete protective next-steps and a free national hotline, so reporting always provides value.

## Handling of unverifiable data
- Reports cannot be independently verified. Veza treats aggregated reports as **early-warning signals**, not confirmed incidents. Patterns are shared with partners only to prompt investigation, never as unverified public alerts.

## Anti-misuse commitments
- Veza publishes its official number publicly and never requests banking details, passwords, or one-time PINs at any point.
- Basic abuse controls (rate-limiting, completion-gating, AI-screening) reduce spam and fake submissions.

## Known ethical limitations
- The builder is not a member of the primary target-language community; native speakers review all translations, and community ambassadors are planned to embed Veza in trusted local structures.
- Data is stored on standard cloud infrastructure managed by a small team; for scale, stronger data-governance and a formal ethics review would be required before expanding collection.
