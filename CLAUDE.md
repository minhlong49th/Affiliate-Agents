# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose
This project builds affiliate landing pages using a 4-agent sequential pipeline.
All output files are saved to `./output/[brand_slug]/` (orchestrator creates subfolder per brand).

## Example invocations

```
Build LP for BuildASoil — affiliate URL /go/buildasoil — GoAffPro — coupon
Build review LP for SeedsNow.com, affiliate /go/seedsnow, network: ShareASale
Build comparison LP for NordicTrack vs Peloton — /go/nordictrack — CJ
```

---

## LP Type Routing

Orchestrator selects `lp_type` from user intent. Do NOT guess — follow this decision tree:

```
keyword contains "coupon" / "promo code" / "discount code"     → coupon
keyword contains "review" / "worth it" / "legit"               → review
keyword contains "vs" / "versus" / "alternative" / "compared"  → comparison
traffic source = facebook / native / youtube                    → advertorial
user says "quiz" / "personalized" / "recommendation"           → quiz
none of the above                                               → coupon (default)
```

`comparison` LP requires `competitor_brand` — ask if missing.

---

## Error / STOP conditions

| Condition | Action |
|---|---|
| `affiliate_url` missing or unverified | STOP. "Affiliate link required. Test in incognito first." |
| `brand_url` returns 403 | Worker 1 uses network data only. Flag "research limited." |
| `lp_type=comparison` and no `competitor_brand` | Ask user before proceeding. |
| `data_quality.flags` includes `AFFILIATE_LINK_UNVERIFIED` | Worker 2 STOPs entire pipeline. |
| `data_quality.flags` includes `COMMISSION_BELOW_FLOOR` | WARN. "Commission < $8/sale. ROAS unlikely positive." |
| `data_quality.flags` includes `RATING_BELOW_THRESHOLD` | WARN. "Brand rating < 3.5 stars. Conversion challenges likely." |
| `data_quality.flags` includes `PPC_POLICY_UNKNOWN` (coupon/review LP) | WARN. "Verify PPC policy before running Google Ads." |

---

## Sub-Agent Routing Rules

**Invoke `lp-orchestrator` when:**
- User provides a brand name + affiliate URL
- User says "build LP", "landing page", "coupon LP", "review LP"
- User provides a keyword like "[brand] coupon" or "[brand] review"

**Never invoke individual workers directly.** Always route through `lp-orchestrator`.

**Sequential dispatch only** — this pipeline is strictly ordered:
`lp-brand-researcher` → `lp-content-builder` → `lp-qa-checker` → `lp-html-generator`

Each agent receives JSON output from the previous step. Do NOT parallelize.

The QA loop runs up to 3 attempts. On the 3rd attempt, QA force-passes regardless of score (flagged "FORCE-PASSED — review required").

---

## Context-passing protocol

Each agent writes its output to a temp JSON file in `./output/[brand_slug]/`:
- Orchestrator → `./output/[brand_slug]/.pipeline_input.json`
- Worker 1 → `./output/[brand_slug]/.brand_data.json`
- Worker 2 → `./output/[brand_slug]/.content_blueprint.json`
- Worker 4 (QA) → `./output/[brand_slug]/.qa_result.json`
- Worker 3 → `./output/[brand_slug]/[brand-slug]-[lp-type]-lp.html`

Temp files (prefixed with `.`) can be deleted after the final HTML is confirmed.

---

## Knowledge files location

All knowledge files are in `./knowledge/`:

**Active (injected by workers):**
- `lp_framework_base.md` — base rules applied to all LP types
- `lp_framework_coupon.md` / `lp_framework_review.md` / `lp_framework_comparison.md`
- `lp_framework_advertorial.md` / `lp_framework_quiz.md`
- `copywriting_techniques.md` — PSBCU, PAS, RSA frameworks
- `html_design_system_lite.md` — CSS variables, components, isolation rules

**Deprecated (retained for human reference, not injected):**
- `html_design_system.md` — use `_lite` version instead
- `qa_rubric_all.md` — rubric is now inline in Worker 4's agent definition

Workers read relevant knowledge files via the Read tool based on `lp_type`.

---

## Agent models (set via frontmatter in `.claude/agents/`)

| Agent | Model | Role |
|---|---|---|
| lp-orchestrator | claude-sonnet-4-6 | Input parsing, LP-type routing, pipeline dispatch |
| lp-brand-researcher | claude-haiku-4-5-20251001 | Fast JSON extraction, low reasoning needed |
| lp-content-builder | claude-sonnet-4-6 | Complex copywriting, framework compliance |
| lp-qa-checker | claude-sonnet-4-6 | Critical scoring, must catch content failures |
| lp-html-generator | claude-haiku-4-5-20251001 | Template rendering, no reasoning needed |

Estimated ~15,000–25,000 tokens per run (with QA pass on first attempt).

---

## Key design constraints

- **CSS isolation**: All HTML is wrapped in `.claude-lp-wrapper` with `all: revert`. All CSS selectors are prefixed with `.claude-lp-wrapper`. No external stylesheets, no CDN fonts.
- **WordPress compatibility**: Output is a self-contained `<style>` + `<div class="claude-lp-wrapper">` + `<script>` block. No `<html>`, `<head>`, or `<body>` tags in the pasted block.
- **Placeholder check**: Worker 3 must scan for `[` characters before saving — no visible placeholder text in output.
- **FTC disclosure**: Mandatory in footer of every LP. Non-negotiable.
- **Affiliate link format**: All outbound links use `[affiliate_url]?utm_source=organic&utm_medium=lp&utm_campaign=[brand-slug]-[lp-type]`.

---

## Post-generation QA checklists

After HTML is generated, the orchestrator outputs these checklists. The user runs them manually.

**Browser QA (after WordPress paste):**
- Reveal button works → brand site opens in new tab
- Coupon code displays, copy button works
- Mobile view: no text overflow, buttons tappable
- Urgency bar correct color (amber = expiry, gray = evergreen)
- Footer disclosure visible
- No `[` placeholder text anywhere on page

**Deploy QA (before Google Ads):**
- Affiliate link tested incognito → correct merchant page + cookie fires
- UTM parameters on all outbound links
- GA4 `coupon_reveal` event fires (GTM Preview + GA4 Realtime)
- PageSpeed Insights mobile score >= 70
- Keywords appear naturally — read LP aloud
