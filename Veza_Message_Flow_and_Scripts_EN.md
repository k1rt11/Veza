# Veza — Complete Message Flow & Scripts (English master)

This is every message the bot sends. The wording is short and plain — for stressed, possibly low-literacy users

---

## 0. SESSION / SPAM RULES (logic, not messages)

- One in-progress report per number at a time.
- Max 3 completed reports per number per day.
- Only a report that completes Q1–Q5 is saved as a record. Partial/abandoned sessions are discarded.
- **Phone number is stripped before the row is written to the sheet.** Generate a random report ID instead.
- Digest opt-in numbers are stored in a SEPARATE sheet/tab, only if the user opts in.

---

## 1. WELCOME (first message the user sees)

> 👋 You're not alone, and this is not your fault.
>
> This week, [N] people in Gauteng reported AI-related scams. Your experience helps protect others.
>
> This takes about 2 minutes. We never store your phone number.
>
> Reply with a number to choose your language:
> 1 — English
> 2 — isiZulu
> 3 — Sesotho

*(If [N] live count is not built yet, use a fixed honest line: "People across Gauteng are reporting AI-related scams.")*

---

## 2. SCREENING QUESTION (after language chosen)

> Did this involve a **fake voice, image, video, or automated messages that did not seem human**?
>
> 1 — Yes
> 2 — No / Not sure

**If 2 (No / Not sure):**

> Thank you. Veza focuses on AI-related scams (like deepfakes or voice clones), so this may be outside what we collect — but you can still get help.
>
> To report any scam or get advice, call the free Yima hotline: **083 123 7226** (connects you to banks, insurers, and police).
>
> Stay safe. 💛

*(End session. No data saved.)*

**If 1 (Yes): continue to Q1.**

---

## 3. THE FIVE QUESTIONS

### Q1 — Type of harm
> What kind of scam was it? Reply with a number:
> 1 — Someone pretended to be a person or company (impersonation)
> 2 — A fake video or photo of a real person (deepfake)
> 3 — A fake investment or "get rich" offer
> 4 — A fake job or work offer
> 5 — False information / fake news
> 6 — Something else

### Q2 — Where it happened
> Where did it happen? Reply with a number:
> 1 — WhatsApp
> 2 — A phone call
> 3 — Facebook
> 4 — Email or SMS
> 5 — Somewhere else

### Q3 — Impact
> What did it affect? Reply with a number:
> 1 — I lost money
> 2 — I gave away personal information
> 3 — It upset me but I lost nothing
> 4 — Nothing happened, I caught it in time

### Q4 — Did you report it
> Did you report this anywhere else?
> 1 — Yes
> 2 — No, I felt ashamed
> 3 — No, I didn't know where to report
> 4 — No, I didn't think it would help

### Q5 — Optional evidence + free text
> Last step (optional). You can:
> • Send a screenshot or voice note, OR
> • Type what happened in your own words, OR
> • Reply SKIP to finish.
>
> Anything you share helps warn others.

*(A human monitor reviews any voice note / screenshot / free text and records key details. Free text is also where NEW scam types surface.)*

> **DESIGN NOTE — elevate storytelling/voice (Track I cares about this a lot).**
> The brief explicitly values voice, storytelling, and local languages. So don't treat the story as a buried "step 5." Two cheap ways to make it first-class:
> 1. **Offer it up front too:** right after the language choice, add — "You can tell us what happened in your own words (just type, or send a voice note), or answer a few quick questions — your choice." This lets a distressed person simply *talk* instead of navigating a form.
> 2. **Always invite the voice/story**, never bury it: phrase Q5 as an invitation ("Tell us in your own words — this is the part that helps most"), not an afterthought.
> The structured questions stay (they power the pattern-clustering); the story path just becomes equally prominent. The human monitor structures whatever comes in.

---

## 4. NEXT-STEPS RESPONSE (sent immediately after Q5)

**Always send this core block:**

> ✅ Thank you. Your report is recorded and helps protect your community.
>
> **What to do now:**
> • Call the free Yima hotline: **083 123 7226** — it connects you to your bank, insurers, and the police.
> • If you lost money or shared banking details, call your bank's fraud line immediately and freeze affected cards/accounts.
> • Do not click any more links from the scammer. Block and delete the contact.
> • Protect yourself from identity theft for free: register at www.safps.org.za (Protective Registration).

**Then add the matching red-flags block based on their Q1 answer:**

**If Q1 = 1 (Impersonation):**
> **Spot it next time:** Real banks, SARS, and the police will NEVER ask for your PIN, password, or a one-time PIN. They will never run an "investigation" over WhatsApp or a video call. If someone rushes you or threatens you — stop and verify by calling the company directly on their official number.

**If Q1 = 2 (Deepfake):**
> **Spot it next time:** A video or voice can be faked. If a known person (a celebrity, official, or even "family") asks for money or promotes an investment, treat it as fake until proven real. Call the real person or organisation on a number you already trust. Urgency + a familiar face is a classic deepfake trick.

**If Q1 = 3 (Fake investment):**
> **Spot it next time:** No real investment "guarantees" returns like 30%. If it promises quick, guaranteed profit and pressures you to deposit fast, it's a scam. Check if the company is registered with the FSCA before sending any money.

**If Q1 = 4 (Job scam):**
> **Spot it next time:** A real employer will never ask you to PAY for a job, training, or "processing fees", and will never ask for your banking PIN. If a job offer comes with upfront costs or seems too easy, it's almost always a scam.

**If Q1 = 5 (False information):**
> **Spot it next time:** Fake news and AI-generated posts spread fast. Before you act on or forward something shocking, check whether a trusted news source reports the same thing. If only one unknown account is saying it, be suspicious.

**If Q1 = 6 (Something else):**
> **Spot it next time:** If a message creates urgency, asks for money or personal details, or seems too good to be true — pause and verify through an official channel before doing anything.

---

## 5. DIGEST OPT-IN (sent last)

> Want a free weekly WhatsApp message showing the latest scams going around and how to spot them? You can forward it to family and friends.
>
> 1 — Yes, send me weekly tips (we'll save only your number for this, and you can stop anytime by replying STOP)
> 2 — No thanks

**If 1:** save number to the SEPARATE digest list. Reply:
> Done! You'll get a short weekly tip. Reply STOP anytime to unsubscribe. Stay safe. 💛

**If 2:** Reply:
> No problem. Stay safe. 💛 (Your number is not stored.)

---

## 6. STOP / UNSUBSCRIBE (if user replies STOP later)
> You've been unsubscribed and your number is deleted. Take care. 💛

---