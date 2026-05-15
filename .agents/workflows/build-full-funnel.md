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

### Step 4 — Brand Research (LP Worker 1)

Run LP Worker 1 from lp-builder-agent skill.
- Input: all collected fields + keyword_list
- Output: brand_data.json → ./output/[brand_slug]/.lp_brand_data.json
- If brand_url returns 403 → proceed with network listing data only, flag it

### Step 5 — Content Blueprint (LP Worker 2)

Run LP Worker 2 from lp-builder-agent skill.
- Input: lp_brand_data.json + lp_type + keyword_list
- Output: content_blueprint.json → ./output/[brand_slug]/.content_blueprint.json

### Step 6 — QA Loop (LP Worker 4) — max 3 attempts

Run LP Worker 4 from lp-builder-agent skill.

attempt = 1
WHILE attempt ≤ 3:
  Score content_blueprint → write .lp_qa_result.json
  IF pass_to_worker_3 = true → break, go to Step 7
  IF attempt < 3 → send revision_instructions to LP Worker 2 → re-run Step 5
  IF attempt = 3 AND still FAIL → force-pass, document issues → go to Step 7
  attempt += 1

RULE: data_quality flags never halt the pipeline. Proceed unconditionally.

### Step 7 — HTML Generation (LP Worker 3)

Run LP Worker 3 from lp-builder-agent skill.
- Input: QA-approved (or force-passed) content_blueprint.json
- Output: production_artifacts/[brand_slug]/[brand-slug]-[lp-type]-lp.html
- All HTML wrapped in <div class="claude-lp-wrapper"> with fully scoped CSS

### Step 8 — LP Phase Summary

Print LP phase result before starting PPC:

LP PHASE COMPLETE
─────────────────────────────────
Brand:      [brand_name]
LP Type:    [lp_type]
Output:     production_artifacts/[brand_slug]/[brand-slug]-[lp-type]-lp.html
Primary KW: [target_keyword]
LP QA:      [PASS / FORCE-PASSED after N attempts]
─────────────────────────────────
Starting PPC phase...

Set landing_page_url = path of HTML file output above.

---

## PHASE 2 — BUILD PPC CAMPAIGN

### Step 9 — LP Analysis (PPC Worker 1)

Run PPC Worker 1 from ppc-affiliate-pipeline skill.
- Input: all collected fields + landing_page_url from Step 7
- LP URL check: SKIP (LP was just built and verified in Phase 1)
- Output: ppc_brand_data.json → ./output/[brand_slug]/.ppc_brand_data.json

### Step 10 — Keyword Generation (PPC Worker 2)

Run PPC Worker 2 from ppc-affiliate-pipeline skill.
- Input: ppc_brand_data.json
- Output: keyword_sets.json → ./output/[brand_slug]/.keyword_sets.json

### Step 11 — Ad Copy Writing (PPC Worker 3)

Run PPC Worker 3 from ppc-affiliate-pipeline skill.
- Input: ppc_brand_data.json + keyword_sets.json
- Output: ad_copy_draft.json → ./output/[brand_slug]/.ad_copy_draft.json

### Step 12 — QA Compliance (PPC Worker 4)

Run PPC Worker 4 from ppc-affiliate-pipeline skill.
- Input: ad_copy_draft.json + keyword_sets.json
- If QA FAIL → fix failing ad groups only, re-run PPC Worker 3 (max 1 retry)
- If still FAIL → force-pass, tag group [NEEDS_MANUAL_REVIEW]
- Output: ppc_qa_result.json → ./output/[brand_slug]/.ppc_qa_result.json

### Step 13 — CSV + Brief Export (PPC Worker 5)

Run PPC Worker 5 from ppc-affiliate-pipeline skill.
- Input: ad_copy_draft.json + keyword_sets.json + ppc_qa_result.json + ppc_brand_data.json
- Output saved to production_artifacts/[brand_slug]/:
  - [brand-slug]-campaign-brief.md
  - [brand-slug]-google-ads.csv
  - [brand-slug]-bing-ads.csv

---

## Step 14 — Final Report

Print combined funnel report:

FULL FUNNEL BUILD COMPLETE
═════════════════════════════════════
Brand:    [brand_name]
LP Type:  [lp_type]

LP OUTPUT
─────────────────────────────────
File:     production_artifacts/[brand_slug]/[brand-slug]-[lp-type]-lp.html
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
  Brief:      production_artifacts/[brand_slug]/[brand-slug]-campaign-brief.md
  Google CSV: production_artifacts/[brand_slug]/[brand-slug]-google-ads.csv
  Bing CSV:   production_artifacts/[brand_slug]/[brand-slug]-bing-ads.csv
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
- Save Location: intermediate JSON → output/[brand_slug]/ | final files → production_artifacts/[brand_slug]/
- Only 1 approval gate: missing competitor_brand on comparison LP (Step 1)
- Phase 1 output (LP HTML path) is automatically passed as landing_page_url to Phase 2 — user does not need to provide it
- LP QA retry cap: 3 attempts | PPC QA retry cap: 1 attempt per ad group
- No silent failures: every flag, force-pass, or skip must appear in the final report