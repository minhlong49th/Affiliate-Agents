---
description: Full-funnel affiliate builder. Runs LP pipeline first (brand research → content → HTML), then automatically chains into PPC pipeline (keywords → ad copy → CSV export) using the LP output as landing page URL.
---

## Objective
Build a complete affiliate funnel in one command: LP first, PPC second. Output is a WordPress-ready HTML landing page + Google Ads and Bing Ads import-ready CSV files.

---

## Instructions

### Step 1 — Collect Inputs

Ask the user ONCE if any REQUIRED field is missing:

- brand_name (required)
- brand_url (required)
- affiliate_url (required)
- network (required, e.g. ShareASale / CJ / GoAffPro)
- lp_type (optional — auto-detect or default to coupon)
- coupon_code (optional — use [COUPON_CODE] placeholder if missing)
- keyword_list (optional — Worker 1 derives if missing)
- competitor_brand (required ONLY if lp_type = comparison)
- niche (optional — derived from brand_url)
- geo (optional — default US)

APPROVAL GATE: If lp_type = comparison AND competitor_brand is missing → stop and ask before proceeding.

NOTE: landing_page_url is NOT required from user — it will be the HTML output from Phase 1.

---

### Step 2 — Hard Stop Protocol (run BEFORE anything else)

Scan brand_name, niche, lp_type for forbidden PPC categories:

FULL STOP — halt entire pipeline immediately:
- Payday loans / cash advance / debt consolidation
- Gambling / casino / sports betting
- Crypto / NFT / passive income / MLM
- Adult / NSFW content
- Prescription drugs or disease cure claims
- Weight loss with clinical claims
- Firearms / weapons / counterfeit goods

PARTIAL STOP — LP builds normally, PPC removes brand keyword groups only:
- Brand name bidding where ppc_policy = restricted

FLAG only (proceed with note):
- If ppc_policy = not_mentioned → flag "PPC policy unconfirmed — verify before launch"

---

## PHASE 1 — BUILD LANDING PAGE

### Step 3 — Route LP Type

Detect lp_type from user input:
- "coupon" / "promo code" / "discount code" → coupon
- "review" / "worth it" / "legit" → review
- "vs" / "versus" / "alternative" → comparison
- traffic source is facebook / native / youtube → advertorial
- "quiz" / "personalized" / "recommendation" → quiz
- (no match) → coupon (default)

Normalize keyword_list to array regardless of format (comma, bullets, JSON).
Compute brand_slug = brand_name lowercase, spaces replaced with hyphens.

### Step 3.5 — Research Cache Check

Before running LP Worker 1, check if brand data already exists:

```
IF ./output/[brand_slug]-[start_running_time]/.lp_brand_data.json EXISTS:
  Check file age: (current_time - file_modified_time) in hours
  IF age < 168 (7 days):
    CACHE HIT → skip LP Worker 1
    Log: "CACHE HIT — reusing lp_brand_data.json for [brand_slug] (age: Xh)"
    Proceed directly to Step 5 (Content Blueprint)
  ELSE:
    CACHE MISS → run LP Worker 1 (file too old)
ELSE:
  CACHE MISS → run LP Worker 1 (no existing data)
```

### Step 4 — Brand Research (LP Worker 1)

Run LP Worker 1 from lp-builder-agent skill.
- Input: all collected fields + keyword_list
- Output: brand_data.json → ./output/[brand_slug]-[start_running_time]/.lp_brand_data.json
- If brand_url returns 403 → proceed with network listing data only, flag it

### Step 5 — Content Blueprint (LP Worker 2)

Run LP Worker 2 from lp-builder-agent skill.
- Input: lp_brand_data.json + lp_type + keyword_list
- Output: content_blueprint.json → ./output/[brand_slug]-[start_running_time]/.content_blueprint.json

### Step 6 — QA Loop (LP Worker 4) — max 3 attempts

Run LP Worker 4 from lp-builder-agent skill.

attempt = 1
WHILE attempt ≤ 3:
  Score content_blueprint → write .lp_qa_result.json
  IF pass_to_worker_3 = true → break, go to Step 7
  IF attempt < 3:
    Extract `pass_section_paths` from .lp_qa_result.json
    Send to LP Worker 2:
      - `revision_instructions` (what to fix)
      - `frozen_sections` = pass_section_paths (what NOT to touch)
    Re-run Step 5 (LP Worker 2 in REVISION MODE — surgical patch only)
  IF attempt = 3 AND still FAIL → force-pass, document issues → go to Step 7
  attempt += 1

RULE: data_quality flags never halt the pipeline. Proceed unconditionally.
RULE: frozen_sections enforcement — LP Worker 2 MUST NOT modify any path in frozen_sections.

### Step 7 — HTML Generation (LP Worker 3)

Run LP Worker 3 from lp-builder-agent skill.
- Input: QA-approved (or force-passed) content_blueprint.json
- Output: `./output/[brand_slug]-[start_running_time]/[brand-slug]-[lp-type]-lp.html`
- All HTML wrapped in `<div class="claude-lp-wrapper">` with fully scoped CSS
- **NOTE:** All final outputs live in `./output/[brand_slug]-[start_running_time]/` — do NOT use `production_artifacts/`

### Step 8 — LP Phase Summary

Print LP phase result before starting PPC:

LP PHASE COMPLETE
─────────────────────────────────
Brand:      [brand_name]
LP Type:    [lp_type]
Output:     ./output/[brand_slug]-[start_running_time]/[brand-slug]-[lp-type]-lp.html
Primary KW: [target_keyword]
LP QA:      [PASS / FORCE-PASSED after N attempts]
─────────────────────────────────
Starting PPC phase...

Set landing_page_url = path of HTML file output above.

---

## PHASE 2 — BUILD PPC CAMPAIGN

### Step 8.5 — Research Cache Check (LP→PPC Handoff)

In Full Funnel mode, LP Phase has already produced brand research. Before invoking PPC-W1:

**Action: Update `./output/[brand_slug]-[start_running_time]/.pipeline_input.json`** — add these fields:
```json
{
  "full_funnel_cache": true,
  "lp_brand_data_path": "./output/[brand_slug]-[start_running_time]/.lp_brand_data.json",
  "landing_page_url": "./output/[brand_slug]-[start_running_time]/[brand-slug]-[lp-type]-lp.html"
}
```

Then log: `"CACHE HIT (Full Funnel) — LP brand_data will be reused for PPC phase"`

### Step 9 — LP Analysis (PPC Worker 1)

Run PPC Worker 1 from ppc-affiliate-pipeline skill.
- Input: all collected fields + `landing_page_url` from Step 7 + **lp_brand_data.json as base context**
- LP URL check: SKIP (LP was just built and verified in Phase 1)
- Brand URL fetch: SKIP (reuse lp_brand_data.json — already researched)
- Only task: fetch and parse `landing_page_url` to extract LP headline, offer, CTA
- Output: `ppc_brand_data.json` → `./output/[brand_slug]-[start_running_time]/.ppc_brand_data.json`

### Step 10 — Keyword Generation (PPC Worker 2)

Run PPC Worker 2 from ppc-affiliate-pipeline skill.
- Input: ppc_brand_data.json
- Output: keyword_sets.json → ./output/[brand_slug]-[start_running_time]/.keyword_sets.json

### Step 11 — Ad Copy Writing (PPC Worker 3)

Run PPC Worker 3 from ppc-affiliate-pipeline skill.
- Input: ppc_brand_data.json + keyword_sets.json
- Output: ad_copy_draft.json → ./output/[brand_slug]-[start_running_time]/.ad_copy_draft.json

### Step 12 — QA Compliance (PPC Worker 4)

Run PPC Worker 4 from ppc-affiliate-pipeline skill.
- Input: ad_copy_draft.json + keyword_sets.json
- If QA FAIL → fix failing ad groups only, re-run PPC Worker 3 (max 1 retry)
- If still FAIL → force-pass, tag group [NEEDS_MANUAL_REVIEW]
- Output: ppc_qa_result.json → ./output/[brand_slug]-[start_running_time]/.ppc_qa_result.json

### Step 13 — CSV + Brief Export (PPC Worker 5)

Run PPC Worker 5 from ppc-affiliate-pipeline skill.
- Input: ad_copy_draft.json + keyword_sets.json + ppc_qa_result.json + ppc_brand_data.json
- Output (save to `./output/[brand_slug]-[start_running_time]/`):
  - `[brand-slug]-campaign-brief.md`
  - `[brand-slug]-google-ads.csv`
  - `[brand-slug]-bing-ads.csv`

---

## Step 14 — Final Report

Print combined funnel report:

FULL FUNNEL BUILD COMPLETE
═════════════════════════════════════
Brand:    [brand_name]
LP Type:  [lp_type]

LP OUTPUT
─────────────────────────────────
File:     ./output/[brand_slug]-[start_running_time]/[brand-slug]-[lp-type]-lp.html
QA:       [PASS / FORCE-PASSED after N attempts]
Keywords: [count] — [list joined by " · "]

PPC OUTPUT
─────────────────────────────────
Ad Groups:    [count]
Headlines:    [count] total
Descriptions: [count] total
Keywords:     [count] total
PPC QA:       [PASS / FORCE-PASSED]
  Approved: [N]   Flagged: [N]
Files:
  Brief:      ./output/[brand_slug]-[start_running_time]/[brand-slug]-campaign-brief.md
  Google CSV: ./output/[brand_slug]-[start_running_time]/[brand-slug]-google-ads.csv
  Bing CSV:   ./output/[brand_slug]-[start_running_time]/[brand-slug]-bing-ads.csv
═════════════════════════════════════
BROWSER QA (after pasting LP into WordPress):
□ Reveal button → brand site opens in new tab
□ Coupon code shows, copy button works
□ Mobile: no overflow, buttons tappable
□ Urgency bar: amber = expiry, gray = evergreen
□ FTC disclosure visible in footer
□ No "[" placeholder text anywhere on page
─────────────────────────────────
DEPLOY QA (before connecting Google Ads):
□ Affiliate link tested incognito → correct merchant + cookie fires
□ UTM params on all outbound links
□ GA4 coupon_reveal event fires
□ PageSpeed mobile score ≥70
□ Read LP aloud — keywords sound natural
□ Verify affiliate PPC policy allows brand keyword bidding
□ Set conversion tracking before going live
□ Set daily budget cap per ad group
□ Quality Score 6 or above before scaling
□ Set auto-pause rule: CPA over threshold for 72hrs
═════════════════════════════════════

---

## Rules of Engagement

- Hard Stop (Step 2) runs before any worker — forbidden category = full stop for both phases
- All outputs (intermediate JSON + final HTML + CSV) → `./output/[brand_slug]-[start_running_time]/`
- Only 1 approval gate: missing competitor_brand on comparison LP (Step 1)
- Phase 1 output (LP HTML path) is automatically passed as landing_page_url to Phase 2 — user does not need to provide it
- LP QA retry cap: 3 attempts | PPC QA retry cap: 1 attempt per ad group
- No silent failures: every flag, force-pass, or skip must appear in the final report