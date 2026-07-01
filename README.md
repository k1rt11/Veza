# Veza — A Community AI Harm Reporting System

**Veza** ("bring to light" in isiZulu) is an open, low-cost WhatsApp tool that lets people in Gauteng report AI-generated scams (deepfakes, voice clones, fake investments) in their own language, get clear guidance on what to do, and help build an early-warning record of AI harm that does not currently exist.

Built for the Africa AI Safety Prize Competition 2026 (Track I: Community-Level Monitoring of AI Harms).

**Current state:** Working prototype, piloted and tested. Delivered over WhatsApp using Twilio's WhatsApp sandbox. A production deployment would use a dedicated WhatsApp number.

## Demo — see the bot working

**Watch the demo video:** https://drive.google.com/file/d/1qeLoaT8ClbDBWGd567n5wmSsJzfkhuB6/view?usp=sharing

**Or try it live:** on WhatsApp, send `join column-event` to `+1 415 523 8886`, then message the bot and follow the prompts. It works in English, isiZulu, and Sesotho.
(The pilot runs on Twilio's WhatsApp sandbox, so the number shown is the Twilio sandbox number, not a branded Veza number.)

The screenshot below shows the Veza service deployed and running live on Render.

![Veza deployment](Image_2026-07-01_at_14_08.jpeg)

---

## What it does

1. A person messages the Veza WhatsApp number.
2. They get a short, shame-reducing welcome and choose a language: English, isiZulu, or Sesotho.
3. A screening question checks whether the harm was AI-related. Non-AI reports are given the Yima hotline and gently exited.
4. They answer five simple multiple-choice questions.
5. They can optionally tell their story in their own words, by voice note or text (or skip).
6. They immediately receive clear next steps plus tips on how to spot that scam next time, in their language.
7. They can opt in to a weekly safety digest.
8. The report is saved (with the phone number never stored). A human reviews voice notes and free text and groups similar reports to reveal patterns.

---

## Why this matters

We cannot make AI safe if we cannot see how it harms people. In South Africa, about 80% of scams go unreported, and existing tools are English-only and website or hotline based. Veza captures AI-harm reports from people who are usually left out, in their own languages, and turns them into a structured record.

---

## Repository contents

- `veza_bot_multilingual.py` — the WhatsApp bot (English, isiZulu, Sesotho), built for Twilio + Flask.
- `veza_ai_scam_checker.py` — a transparent, rule-based scam-likelihood checker (explainable by design, no black-box model).
- `requirements.txt` — Python dependencies.
- `Procfile` — for deployment (e.g. Render).
- `Veza_Message_Flow_and_Scripts_EN.md` — every message the bot sends, in order (English source of truth).
- `Veza_Model_Evaluation_Results.md` — a model-failure evaluation of AI translation on isiZulu and Sesotho scam phrases.

---

## How it works technically

The bot is a Flask web service. Twilio forwards incoming WhatsApp messages to a `/whatsapp` endpoint, and the bot replies. The conversation is simple branching logic: each numbered reply leads to the next message. No AI model is needed to run the flow.

Reports are appended to a CSV file. Each report is stored against a random report ID, and the phone number is never written to storage.

### Setup

1. **Twilio WhatsApp sandbox:** create a free Twilio account, open the WhatsApp sandbox, and note the sandbox number and join code. Testers send the join code once, then can use the bot over WhatsApp.
2. **Deploy the bot:** host `veza_bot_multilingual.py` (a free tier such as Render works for a pilot).
   - Install: `pip install -r requirements.txt`
   - Start: `gunicorn veza_bot_multilingual:app`
3. **Connect Twilio:** in the sandbox settings, set "When a message comes in" to `https://YOUR-APP-URL/whatsapp` (POST).
4. **Test:** message the sandbox number and follow the prompts.

To run locally instead, use `python veza_bot_multilingual.py` plus a tunnel (such as ngrok) to expose the `/whatsapp` endpoint to Twilio.

---

## Privacy and responsible design

- The reporter's phone number is never stored. It is hashed in memory only during the chat, then discarded, so reports cannot be traced back.
- Voice notes and screenshots are optional and are human-reviewed and summarised, not stored at scale.
- The scam checker is rule-based and explainable, not a hidden model.
- Veza never asks for banking details, passwords, or OTPs, and publishes its official number to prevent copies.

---

## How patterns are found

A human reviewer reads new reports each week. The rule used in the pilot: 3 or more reports with the same harm type and the same channel within 7 days are flagged as an emerging pattern. A pattern is an early-warning signal for partners to check, not proof and not a public alert.

---

## Honest limitations

- This is a pilot. It shows the system works and the grouping rule runs. It does not yet prove real patterns at scale.
- Reports cannot be verified.
- Translations are machine-drafted and were checked by the team using back-translation, because a native speaker was not available in time. Native-speaker review is a next step.
- The reviewer role is one unpaid person.
- The pilot runs on Twilio's WhatsApp sandbox (a shared test number) and free-tier hosting, which has cold-start delay.

---

## Adapting Veza to your context

- **New language:** copy the English scripts, translate them, and add them to the bot.
- **New harm categories:** edit the question options and add a matching "spot it next time" tip.
- **New region:** change the local fraud-reporting contacts in the next-steps message.
