# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose
Two independent pipelines sharing one project:
- **LP Builder** — builds affiliate landing pages (HTML output)
- **PPC Ad Copy Builder** — builds Google Ads / Bing Ads campaigns (CSV + brief output)

Both can run independently or back-to-back on the same brand.

All LP output files are saved to `./output/[brand_slug]/` (orchestrator creates subfolder per brand).
All PPC output files are saved to `./output/[brand_slug]/` (orchestrator creates subfolder per brand).

---

## Pipeline Routing — read this first

```
INPUT contains LP URL + "build LP" / "landing page" / "coupon LP" / "review LP"
  → Dispatch lp-orchestrator

INPUT contains LP URL + "PPC" / "Google Ads" / "Bing Ads" / "ad copy" / "campaign" / "RSA"
  → Dispatch ppc-orchestrator

INPUT contains BOTH "LP" and "PPC" / "full funnel" / "LP + ads" / "build everything"
  → Run lp-orchestrator FIRST, then ppc-orchestrator
  → ppc-orchestrator uses LP output URL as landing_page_url input

INPUT contains campaign performance data (Clicks / CTR / Conversions table)
  → Dispatch ppc-orchestrator in kill_scale mode

INPUT is ambiguous
  → Ask: "Build LP, PPC campaign, or both?"
```

## Example invocations

```
Build LP for BuildASoil — affiliate URL /go/buildasoil — GoAffPro — coupon
Build review LP for SeedsNow.com, affiliate /go/seedsnow, network: ShareASale
Build comparison LP for NordicTrack vs Peloton — /go/nordictrack — CJ
Build Google Ads campaign for https://buildasoil.com/coupon — platform: both
Build LP and PPC for BuildASoil, affiliate /go/buildasoil, platform: both
Analyze these campaigns: [paste performance table]
```

---

## LP BUILDER PIPELINE

**Trigger phrases:** "build LP", "landing page", "coupon LP", "review LP", "comparison LP", "[brand] LP"

**Agent routing:** Invoke `lp-orchestrator`. Never invoke individual LP workers directly.

**Sequential dispatch:**
```
lp-orchestrator
  → lp-brand-researcher    (Haiku — brand research JSON)
  → lp-content-builder     (Sonnet — content blueprint JSON)
  → lp-qa-checker          (Sonnet — QA loop, max 3 attempts)
  → lp-html-generator      (Haiku — WordPress-ready HTML)
```

### LP Type Routing

```
keyword contains "coupon" / "promo code" / "discount code"     → coupon
keyword contains "review" / "worth it" / "legit"               → review
keyword contains "vs" / "versus" / "alternative" / "compared"  → comparison
traffic source = facebook / native / youtube                    → advertorial
user says "quiz" / "personalized" / "recommendation"           → quiz
none of the above                                               → coupon (default)
```

`comparison` LP requires `competitor_brand` — ask if missing.

### LP Context-passing protocol
- Orchestrator → `./output/[brand_slug]/.pipeline_input.json`
- Worker 1 → `./output/[brand_slug]/.brand_data.json`
- Worker 2 → `./output/[brand_slug]/.content_blueprint.json`
- Worker 4 (QA) → `./output/[brand_slug]/.qa_result.json`
- Worker 3 → `./output/[brand_slug]/[brand-slug]-[lp-type]-lp.html`

### LP Knowledge files (`./knowledge/`)
- `lp_framework_base.md`, `lp_framework_coupon.md`, `lp_framework_review.md`, `lp_framework_comparison.md`
- `lp_framework_advertorial.md`, `lp_framework_quiz.md`
- `copywriting_techniques.md`, `html_design_system_lite.md`
- Deprecated: `html_design_system.md`, `qa_rubric_all.md`

---

## PPC PIPELINE

**Trigger phrases:** "build campaign", "Google Ads", "Bing Ads", "ad copy", "RSA", "PPC", "keyword list"

**Agent routing:** Invoke `ppc-orchestrator`. Never invoke individual PPC workers directly.

**Mode detection (ppc-orchestrator handles this):**
```
performance data (CTR/Conversions) → kill_scale mode
single LP URL                     → single mode
```

**Sequential dispatch:**
```
ppc-orchestrator
  → ppc-lp-analyst         (Haiku — LP fetch, HS-1 policy check, strategy)
  → ppc-keyword-builder    (Haiku — keywords + 3-tier negatives)
  → ppc-ad-copy-writer     (Sonnet — RSA 15H/4D + extensions)
  → ppc-qa-compliance      (Sonnet — policy QA + auto-fix, max 3 attempts)
  → ppc-output-exporter    (Haiku — campaign brief .md + CSV files)
```

### PPC Context-passing protocol
- Orchestrator → `./output/[brand_slug]/.pipeline_input.json`
- Worker 1 → `./output/[brand_slug]/.brand_data.json`
- Worker 2 → `./output/[brand_slug]/.keyword_sets.json`
- Worker 3 → `./output/[brand_slug]/.ad_copy_draft.json`
- Worker 4 (QA) → `./output/[brand_slug]/.qa_result.json`

### PPC Final output
- `./output/[brand_slug]/[brand-slug]-[platform]-campaign-brief.md`
- `./output/[brand_slug]/[brand-slug]-google-ads-import.csv`
- `./output/[brand_slug]/[brand-slug]-bing-ads-import.csv`

### PPC Reference files (`./references/`)
- `00-compact-digest.md` — master index (Sections A–I)
- `00-knowledge-base.md` — brand research & competitor data
- `01-lp-analysis-protocol.md` — LP fetch & extraction workflow
- `02-adgroup-strategy.md` — ad group strategy selection
- `03-keyword-strategy.md` — keyword generation rules
- `04-negative-keywords.md` — 3-tier negative keyword framework
- `05-rsa-copywriting.md` — RSA copywriting frameworks
- `06-policy-compliance.md` — full QA checklist
- `07-output-formats.md` — CSV column specs
- `08-prompt-templates.md` — agent prompt templates
- `08-prompt-templates-archive.md` — archived/legacy templates
- `09-batch-workflow.md` — batch processing protocol
- `10-ad-extensions.md` — sitelink/callout/snippet library
- `11-installation-guide.md` — setup & usage guide

### PPC Templates (`./templates/`)
- `google-ads-import.csv`, `bing-ads-import.csv`

---

## Full Funnel Mode (LP + PPC together)

1. Run LP pipeline first → get HTML output path
2. Use that LP's URL as `landing_page_url` for PPC pipeline
3. Report both outputs together at the end

---

## Hard Stops (both pipelines)

| Code | Trigger | Pipeline | Action |
|------|---------|----------|--------|
| HS-1 | Brand bans PPC in affiliate terms | PPC only | Stop PPC. LP can still run. |
| HS-2 | LP URL unreachable | PPC only | Stop PPC pipeline. |
| LP-ERR | Affiliate link unverified | LP only | Stop LP pipeline. |

## LP Error / Warnings

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

## Agent models (set via frontmatter in `.claude/agents/`)

| Agent | Model | Role |
|---|---|---|
| lp-orchestrator | sonnet | Input parsing, LP-type routing, pipeline dispatch |
| lp-brand-researcher | haiku | Fast JSON extraction, low reasoning needed |
| lp-content-builder | sonnet | Complex copywriting, framework compliance |
| lp-qa-checker | sonnet | Critical scoring, must catch content failures |
| lp-html-generator | haiku | Template rendering, no reasoning needed |
| ppc-orchestrator | sonnet | Input parsing, mode detection, pipeline dispatch |
| ppc-lp-analyst | haiku | LP fetch, PPC policy check, strategy selection |
| ppc-keyword-builder | haiku | Keyword generation, negative keyword lists |
| ppc-ad-copy-writer | sonnet | RSA ad copy, ad extensions |
| ppc-qa-compliance | sonnet | Policy compliance QA, auto-fix, kill/scale analysis |
| ppc-output-exporter | haiku | Campaign brief markdown, CSV export |

Estimated ~15,000–25,000 tokens per LP run (with QA pass on first attempt).
Estimated ~18,000–28,000 tokens per PPC run (both platforms).
Estimated ~30,000–48,000 tokens for full funnel LP + PPC.

---

## Key design constraints (LP Builder)

- **CSS isolation**: All HTML is wrapped in `.claude-lp-wrapper` with `all: revert`. All CSS selectors are prefixed with `.claude-lp-wrapper`. No external stylesheets, no CDN fonts.
- **WordPress compatibility**: Output is a self-contained `<style>` + `<div class="claude-lp-wrapper">` + `<script>` block. No `<html>`, `<head>`, or `<body>` tags in the pasted block.
- **Placeholder check**: Worker 3 must scan for `[` characters before saving — no visible placeholder text in output.
- **FTC disclosure**: Mandatory in footer of every LP. Non-negotiable.
- **Affiliate link format**: All outbound links use `[affiliate_url]?utm_source=organic&utm_medium=lp&utm_campaign=[brand-slug]-[lp-type]`.

---

## Post-generation QA checklists

### LP Builder

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

### PPC Builder

After CSV/brief generated, the orchestrator outputs:

**Before Launching:**
- Test LP URL live in incognito
- Verify coupon code is active (if applicable)
- Confirm PPC allowed in affiliate terms
- Set daily budget + Manual CPC bidding
- Review all MANUAL REVIEW REQUIRED items before submission
- Set up conversion tracking BEFORE launching
- Bing: enable search partners exclusion if applicable

## Cleanup temp files
```bash
rm ./output/*/.*json
```
