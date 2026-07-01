# Do AI Translation Models Preserve Safety-Critical Instructions in Low-Resource African Languages?
### A focused evaluation in the context of fraud-prevention messaging

**A Veza evaluation report — Africa AI Safety Prize Competition 2026**

---

## Summary

As AI systems are deployed to deliver safety-critical information across languages, an under-examined risk is **whether automated translation preserves the *meaning* of safety instructions** — not just general fluency. A fraud-prevention message that says "never share your OTP" is only protective if it still says that after translation. We evaluated whether a widely-used machine translation system preserves safety-critical, fraud-prevention instructions when translating into isiZulu and Sesotho — two languages spoken by millions of South Africans but under-served by AI. We find that while general meaning is mostly preserved, **functional and instructional content degrades**, including at least one failure that would directly prevent a user from acting correctly. This supports a concrete AI-safety conclusion: **automated translation should not be trusted, unreviewed, for safety-critical messaging in low-resource languages**, and a human must remain in the loop.

---

## Why this matters (the AI-safety framing)

Deploying AI to communicate safety information to vulnerable populations is increasingly common. But translation quality is usually measured by general fluency metrics (e.g. BLEU), which do not capture whether a *specific safety instruction survives*. In a fraud-prevention context, the cost asymmetry is severe: a single degraded instruction ("do not share your PIN", "reply X to opt out") can cause direct harm or strand a user mid-process. This evaluation treats **preservation of safety-critical instructions** as the metric that matters, which is the relevant safety property for this deployment context.

## Method

- **Model evaluated:** Google Translate (the most accessible system for these languages).
- **Test set:** 24 short fraud-reporting and safety-instruction phrases (12 isiZulu, 12 Sesotho), drawn from the live Veza reporting tool, including safety-critical instructions (OTP/PIN warnings, FSCA-verification advice) and functional instructions (how to skip a step).
- **Procedure:** Back-translation round-trip (English → target language → English), comparing the round-trip output to the original. This lets a non-native evaluator assess meaning preservation. Ratings: **Correct** (meaning preserved), **Partial** (gist preserved, detail lost), **Wrong** (meaning changed), **Hallucinated** (invented content).
- **Limitation of method:** Back-translation tests written, clean text — the *easy* case. Real reports are conversational voice, code-switched, and dialectal, where degradation is expected to be worse (cf. WAXAL-NET 2026, which found state-of-the-art speech models hallucinate on conversational African speech and do not support most of these languages).

## Results

**General-meaning content was mostly preserved.** Of 24 phrases, roughly 20 retained core meaning (Correct), with minor drift in several ("frozen account" → "closed/blocked account"; "scam" drifting toward "theft"). No hallucinations were observed on this clean test set.

**Safety-critical warnings largely survived** — the OTP/PIN warnings and FSCA-verification advice retained their protective meaning, which is reassuring.

**Functional/instructional content failed.** The instruction **"reply SKIP to finish"** was mistranslated in Sesotho such that the back-translation rendered it as **"reply and be careful to finish"** — the action word "skip" was confused with "take care." A user following the translated instruction would not know how to skip the step. This is a **direct functional failure of a safety/usability instruction caused by automated translation.**

| Category | Result |
|---|---|
| General meaning preserved (Correct) | ~20 / 24 |
| Minor drift (Partial) | ~3 / 24 |
| Functional/instruction failure (Wrong) | ≥1 (the "SKIP" instruction, Sesotho) |
| Hallucinations | 0 (on clean text) |

*(Full per-phrase table available in the project repository.)*

## Finding & implication

The headline result is **not** "machine translation is useless" — on clean text it is largely adequate for *general* meaning. The finding is sharper and more useful: **automated translation degrades exactly the content where errors are most dangerous — precise, functional, instructional language — while performing acceptably on general prose.** A user told the wrong keyword cannot complete an action; a subtly altered safety instruction can mislead. And this is the *best* case (clean written text); conversational, dialectal, code-switched real-world input is expected to fail more often.

**AI-safety conclusion:** In safety-critical, low-resource-language deployments, automated translation must not be used unreviewed. A human reviewer must validate safety-critical and instructional strings before they reach users. This is precisely the design choice Veza makes — it uses fixed, human-reviewed strings and a human monitor for free-text/voice, rather than live machine translation of user input.

## Limitations of this evaluation

Single model; small (n=24), clean-text test set; back-translation is an imperfect proxy (errors can occur in *either* translation direction); a native speaker was not available in time, so the translations were checked by the team using this back-translation method. This is a focused indicative finding, not a comprehensive benchmark. A fuller study would test multiple models, native-speaker forward-evaluation, and real conversational/voice inputs, which are the conditions under which we expect worse results.

---

*Reproducibility: test phrases, full results table, and method are in the Veza open-source repository.*
