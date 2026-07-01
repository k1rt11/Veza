"""
Veza AI-Scam Checker
====================
A transparent, rule-based classifier that helps a user judge whether a
suspicious message, call, video, or voice note shows signs of an AI-driven scam.

WHY THIS IS AN AI-SAFETY COMPONENT (and why it is rule-based on purpose):
- It is *interpretable by design*. Every output is traceable to specific,
  documented warning signs - there is no opaque model the user must trust.
  In a high-stakes, low-resource-language context, an explainable heuristic is
  a safer choice than a black-box classifier whose errors users cannot see.
- It separately flags signals of SYNTHETIC MEDIA (deepfakes / voice clones),
  the frontier misuse case of generative AI, so reports can be triaged for
  AI-specific harm rather than general fraud.
- The red flags are adapted from published guidance by the Southern African
  Fraud Prevention Service (SAFPS) and Yima (yima.org.za).

Run:  python veza_ai_scam_checker.py        # interactive demo
Import: from veza_ai_scam_checker import score_report
"""

from dataclasses import dataclass


# Each indicator: (key, question, weight, is_synthetic_media_signal)
INDICATORS = [
    ("unsolicited",   "Was the contact unexpected / out of the blue?",                                   1, False),
    ("urgency",       "Did they pressure you to act fast or threaten consequences?",                      2, False),
    ("asked_secret",  "Did they ask for a PIN, password, OTP, banking login, or ID number?",             3, False),
    ("too_good",      "Did it promise guaranteed or unusually high returns, a prize, or easy money?",     3, False),
    ("known_person",  "Did a known person/official/celebrity (in a video, voice, or message) ask for "
                      "money or endorse an offer?",                                                       3, True),   # deepfake signal
    ("fake_authority","Did someone claim to be police/SARS/your bank running an 'investigation' or "
                      "threatening arrest, over WhatsApp / phone / video?",                               3, False),
    ("click_install", "Did they ask you to click a link or install an app?",                              2, False),
    ("odd_payment",   "Did they ask for payment by voucher, crypto, or a payment link?",                  2, False),
    ("upfront_fee",   "Did they ask for an upfront fee (for a job, loan, prize, or delivery)?",           2, False),
    ("robotic",       "Did the voice sound robotic/unnatural, or the video look slightly 'off'?",         2, True),   # synthetic-media signal
]

MAX_SCORE = sum(w for _, _, w, _ in INDICATORS)  # 23


@dataclass
class Result:
    score: int
    max_score: int
    risk: str               # "low" | "medium" | "high"
    ai_signal: bool         # synthetic-media (deepfake/voice clone) indicators present
    fired: list             # list of human-readable reasons that contributed


def score_report(answers: dict) -> Result:
    """
    answers: dict mapping indicator key -> bool (True = yes, this was present).
    Missing keys are treated as False.
    Returns a Result with a transparent breakdown.
    """
    score = 0
    ai_signal = False
    fired = []
    for key, question, weight, is_ai in INDICATORS:
        if answers.get(key):
            score += weight
            fired.append(f"{question} (+{weight})")
            if is_ai:
                ai_signal = True

    if score <= 3:
        risk = "low"
    elif score <= 8:
        risk = "medium"
    else:
        risk = "high"

    return Result(score=score, max_score=MAX_SCORE, risk=risk,
                  ai_signal=ai_signal, fired=fired)


def verdict_message(r: Result) -> str:
    """Plain-language output suitable for sending to a user."""
    headline = {
        "low":    "⚠️ A few warning signs. Stay cautious and verify before acting.",
        "medium": "⚠️⚠️ Several warning signs - treat this with strong caution.",
        "high":   "🛑 STOP. This shows strong signs of a scam. Do not engage, pay, or share anything.",
    }[r.risk]

    lines = [headline, f"(Risk score: {r.score}/{r.max_score})"]

    if r.ai_signal:
        lines.append(
            "🤖 This shows signs of AI-generated content (a fake voice or video). "
            "A familiar face or voice can be faked - verify the real person/organisation "
            "on a number you already trust."
        )

    if r.fired:
        lines.append("Why we flagged this:")
        for reason in r.fired:
            # strip the weight annotation for the user-facing version
            lines.append("• " + reason.split(" (+")[0])

    lines.append(
        "\nWhat to do: call the free Yima hotline 083 123 7226 (connects you to your "
        "bank, insurers, and police). Never share your PIN, password, or OTP."
    )
    return "\n".join(lines)


# ---- interactive demo -------------------------------------------------------
def _demo():
    print("Veza AI-Scam Checker - answer y/n to each question.\n")
    answers = {}
    for key, question, _w, _ai in INDICATORS:
        ans = input(f"{question} (y/n) ").strip().lower()
        answers[key] = ans.startswith("y")
    print("\n" + "=" * 60)
    print(verdict_message(score_report(answers)))


if __name__ == "__main__":
    _demo()
