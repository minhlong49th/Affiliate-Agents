---
description: Build Google Ads and Bing Ads affiliate campaigns. Supports single brand, batch, and kill/scale analysis modes. Outputs campaign brief + import-ready CSV files for both platforms.
---

## Objective
Build Google Ads and Bing Ads affiliate campaigns from brand inputs or performance data. Runs a 5-worker pipeline and exports campaign briefs + import-ready CSV files.
 
---
 
## Instructions
 
### Step 1 — Collect Inputs & Detect Mode
 
**MODE = kill_scale** → if user provides performance data (impressions, clicks, ROAS, CPA, etc.)
**MODE = batch** → if user provides multiple brands
**MODE = single** → default
 
For MODE = single, collect the following. Ask the user ONCE if REQUIRED fields are missing:
 
| Field | Required | Default |
|---|---|---|
| `brand_name` | ✅ | — |
| `brand_url` | ✅ | — |
| `affiliate_url` | ✅ | — |
| `network` | ✅ | — |
| `landing_page_url` | ✅ | — |
| `lp_type` | optional | coupon |
| `coupon_code` | optional | — |
| `target_keyword` | optional | derived by Worker 2 |
| `niche` | optional | derived from brand_url |
| `geo` | optional | US |
 
For MODE = batch: collect `brands[]` array. Skip brands missing `brand_url` or `landing_page_url`, log each skip.
For MODE = kill_scale: collect `performance_data[]` with per-campaign metrics.
 
---
 
### Step 2 — Hard Stop Protocol (run BEFORE anything else)
 
**HS-1 — Policy Check**
 
Scan `niche`, `brand_name`, `lp_type` for forbidden categories:
 
FULL STOP (⛔) — output error and halt pipeline:
- Payday loans / cash advance / debt consolidation
- Gambling / casino / sports betting
- Crypto / NFT / passive income / MLM
- Adult / NSFW content
- Prescription drugs or disease cure claims (also: ad copy MUST NOT reference prescription drug names like finasteride, minoxidil, tretinoin, etc. — see QA Section J)
- Weight loss with clinical claims
- Firearms / weapons / counterfeit goods
PARTIAL STOP (⚠️) — remove brand keyword groups, continue with non-brand only:
- Brand name bidding where `ppc_policy = restricted`
FLAG only (proceed) — if `ppc_policy = not_mentioned`: note "PPC policy unconfirmed — verify with network before launch."
FLAG (health niche) — if niche ∈ {hair loss, skincare, health, wellness, supplements}: note "Health/pharma niche detected. Ensure ad copy uses zero prescription drug names (finasteride, minoxidil, etc.). See QA Section J for blacklist."
 
**HS-2 — URL Check**
 
If `brand_url` or `landing_page_url` is missing in single mode → stop and ask.
If batch mode → skip the offending brand, log it, continue with the rest.
 
---
 
### Step 3 — Mode Routing
 
**If MODE = kill_scale:**
Run ppc-qa-compliance skill in KILL_SCALE_ANALYSIS mode.
Output a structured optimization report (kill / scale / pause recommendations per campaign).
STOP — do not proceed to Step 4.
 
**If MODE = batch:**
Run Steps 4–8 for each brand sequentially.
Accumulate per-brand summaries → compile batch report at the end.
 
**If MODE = single:**
Proceed to Step 4.
 
---
 
### Step 3.5 — Research Cache Check

Before running Worker 1, check if brand data already exists to reuse it and skip W1:

```text
IF FULL FUNNEL MODE (invoked from /build-lp):
  Copy ./output/[brand_slug]-[start_running_time]/.lp_brand_data.json → .ppc_brand_data.json
  CACHE HIT → skip Worker 1 (pure file operation, no LLM call needed)
  Proceed directly to Step 5

ELSE (STANDALONE PPC MODE):
  Find most recent .lp_brand_data.json OR .ppc_brand_data.json for [brand_slug] in ./output/
  IF EXISTS and file age < 168 hours (7 days):
    Copy to current run's directory as .ppc_brand_data.json
    CACHE HIT → skip Worker 1
    Log: "CACHE HIT — reusing data for [brand_slug] (age: Xh)"
    Proceed directly to Step 5
  ELSE:
    CACHE MISS → run Worker 1
```

### Step 4 — LP Analysis (Worker 1)
 
Run Worker 1 from ppc-affiliate-pipeline skill.
- Input: all collected fields
- Output: `ppc_brand_data.json` → `./output/[brand_slug]-[start_running_time]/.ppc_brand_data.json`
- If `landing_page_url` returns 404 → use `brand_url` as substitute for analysis only, flag it
---
 
### Step 5 — Keyword Generation (Worker 2)
 
Run Worker 2 from ppc-affiliate-pipeline skill.
- Input: `brand_data.json`
- Output: `keyword_sets.json` → `./output/[brand_slug]-[start_running_time]/.keyword_sets.json`
---
 
### Step 6 — Ad Copy Writing (Worker 3)
 
Run Worker 3 from ppc-affiliate-pipeline skill.
- Input: `brand_data.json` + `keyword_sets.json`
- Output: `ad_copy_draft.json` → `./output/[brand_slug]-[start_running_time]/.ad_copy_draft.json`
---
 
### Step 7 — QA Compliance (Worker 4)
 
Run Worker 4 from ppc-affiliate-pipeline skill.
- Input: `ad_copy_draft.json` + `keyword_sets.json`
- If QA FAIL → fix failing ad groups only, re-run Worker 3 for those groups (max 1 retry)
- If still FAIL after retry → force-pass, tag group `[NEEDS_MANUAL_REVIEW]`
- Output: `qa_result.json` → `./output/[brand_slug]-[start_running_time]/.qa_result.json`
---
 
### Step 8 — CSV + Brief Export (Worker 5)
 
Run Worker 5 from ppc-affiliate-pipeline skill.
- Input: `ad_copy_draft.json` + `keyword_sets.json` + `qa_result.json` + `brand_data.json`
- Output (save to `./output/[brand_slug]-[start_running_time]/`):
  - `[brand-slug]-campaign-brief.md`
  - `[brand-slug]-google-ads.csv`
- **Post-Worker Script (Bing CSV Generation):**
  - Read `[brand-slug]-google-ads.csv`
  - Find & Replace tracking parameters if needed (e.g., `utm_source=google` → `utm_source=bing`)
  - Save as `[brand-slug]-bing-ads.csv`
---
 
### Step 9 — Output Report
 
Print final report:
 
```
PPC BUILD COMPLETE
─────────────────────────────────
Brand:         [brand_name]
Mode:          [mode]
Ad Groups:     [count]
Headlines:     [count] total ([N] per group)
Descriptions:  [count] total ([N] per group)
Keywords:      [count] total
 
QA RESULT: [PASS / FORCE-PASSED]
  Approved groups: [N]   Flagged: [N]
 
OUTPUT FILES:
  📄 Brief:      ./output/[brand_slug]-[start_running_time]/[brand-slug]-campaign-brief.md
  📊 Google CSV: ./output/[brand_slug]-[start_running_time]/[brand-slug]-google-ads.csv
  📊 Bing CSV:   ./output/[brand_slug]-[start_running_time]/[brand-slug]-bing-ads.csv
─────────────────────────────────
PRE-LAUNCH CHECKLIST:
□ Verify affiliate PPC policy allows brand keyword bidding
□ Set conversion tracking before going live
□ Set daily budget cap per ad group
□ Quality Score ≥6 before scaling spend
□ Check trademark restrictions on each keyword
□ Confirm LP URL is live and loading correctly
□ Test affiliate link incognito — cookie fires correctly
□ Set auto-pause rule: CPA > $X for 72hrs
─────────────────────────────────
```
 
---
 
## Rules of Engagement
 
- **Hard stops run first, always** — HS-1 and HS-2 execute before any worker
- **Save Location:** All intermediate JSON + all final outputs → `./output/[brand_slug]-[start_running_time]/`
- **QA retry cap:** max 1 retry per failing ad group, then force-pass with `[NEEDS_MANUAL_REVIEW]` tag
- **Batch resilience:** one brand failing never halts the rest — log and continue
- **Kill/scale mode is read-only:** no keywords or ad copy generated, optimization report only
- **No silent failures:** every HS trigger, skip, flag, or force-pass must appear in the output report
---
 
## Full-Funnel Entry Point
 
If this workflow was invoked from `/build-lp` full-funnel mode:
- `landing_page_url` = HTML output path from `/build-lp`
- Skip LP URL check (already verified by LP pipeline)
- Proceed directly to Step 2 Hard Stop