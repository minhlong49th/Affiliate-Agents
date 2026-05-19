# KNOWLEDGE: LP Framework Coupon (FULL)

## 5. JOEY BABINEAU — PSBCU FRAMEWORK
Simplified (P + B + CU) for Coupon LP. Skip Story entirely.

P = **Problem** — Open with user's specific pain/situation. Not brand description.
B = **Benefit** — Specific outcome the user gets. Not a feature. ("As a result, you..." → keep)
C = **CTA** — Action verb, benefit-driven button text. Name the outcome, not the action.
U = **Urgency** — Real urgency only. Never fake counters or timers.

### PSBCU Application for Coupon LP Intro (~100 words)

```
[P] Open with user's specific pain/situation — 2-3 sentences.
[B] Specific outcome from switching to this brand — with verifiable details.
[C] CTA pointing to coupon box below.
[U] Real verified status or deadline — no fake counters.
```

### Urgency Rules

| Allowed (real urgency) | Banned (fake urgency) |
|---|---|
| "Code verified May 2026 — rechecked monthly" | "Used 22 times today" (fake counter) |
| "Limited stock on [specific strain]" (only if verified on site) | "Last checked 10 mins ago" (hardcoded) |
| "Sale ends when inventory clears" (only if active sale) | "Limited Time" without specific deadline |
| "Code active as of [month year]" | Countdown timers that reset |
| Expiry date from brand_data (only if confirmed) | Dynamic counters that increment on page load |

## 9. MICRO-REVEAL MECHANIC (Coupon LP)
Psychological mechanism: user must perform an action to receive value → micro-commitment increases perceived value of the coupon and brand trust.
Implementation:
- Pre-reveal state: button "Click to Reveal Your Code"
- Post-reveal state: code displayed + copy button + visit brand button
- GA4 event fires on reveal click: `coupon_reveal` event

## AGITATE RULES FOR COUPON
- Brand overview paragraph: One paragraph only. Open with user's pain per PSBCU P (Problem) → introduce brand as solution (Benefit).
- FAQ questions: write from perspective of skeptical or burned user.
- Follow 3-step FAQ answer structure from `copywriting_techniques.md`: Acknowledge → Resolve → Preempt.
