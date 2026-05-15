---
description: Build affiliate landing pages (coupon, review, comparison, advertorial, quiz) from brand inputs. Runs 4-worker pipeline → outputs WordPress-ready HTML file with scoped CSS and FTC disclosure.
---

## Objective
Build a WordPress-ready affiliate landing page from brand inputs. Orchestrates 4 workers via the lp-builder-agent skill.

---

## Instructions

### Step 1 — Collect Inputs

Gather the following. Ask the user ONCE if any REQUIRED field is missing:

- brand_name (required)
- brand_url (required)
- affiliate_url (required)
- network (required, e.g. ShareASale / CJ / GoAffPro)
- lp_type (optional — auto-detect or default to coupon)
- coupon_code (optional — use [COUPON_CODE] placeholder if missing)
- keyword_list (optional — Worker 1 will derive if missing)
- competitor_brand (required ONLY if lp_type = comparison)

APPROVAL GATE: If lp_type = comparison AND competitor_brand is missing → stop and ask before proceeding.

---

### Step 2 — Route LP Type

Detect lp_type from user input:
- "coupon" / "promo code" / "discount code" → coupon
- "review" / "worth it" / "legit" → review
- "vs" / "versus" / "alternative" → comparison
- traffic source is facebook / native / youtube → advertorial
- "quiz" / "personalized" / "recommendation" → quiz
- (no match) → coupon (default)

Normalize keyword_list to array regardless of format (comma, bullets, JSON).
Compute brand_slug = brand_name lowercase, spaces replaced with hyphens.

---

### Step 3 — Brand Research (Worker 1)

Run Worker 1 from lp-builder-agent skill.
- Input: all collected fields + keyword_list
- Output: brand_data JSON → ./output/[brand_slug]/.brand_data.json
- If brand_url returns 403 → proceed with network listing data only, flag it in report

---

### Step 4 — Content Blueprint (Worker 2)

Run Worker 2 from lp-builder-agent skill.
- Input: brand_data.json + lp_type + keyword_list
- Output: content_blueprint.json → ./output/[brand_slug]/.content_blueprint.json

---

### Step 5 — QA Loop (Worker 4) — max 3 attempts

Run Worker 4 from lp-builder-agent skill.

attempt = 1
WHILE attempt ≤ 3:
  Score content_blueprint → write .qa_result.json
  IF pass_to_worker_3 = true → break, go to Step 6
  IF attempt < 3 → send revision_instructions to Worker 2 → re-run Step 4
  IF attempt = 3 AND still FAIL → force-pass, document all issues → go to Step 6
  attempt += 1

RULE: data_quality flags never halt the pipeline. Proceed unconditionally.

---

### Step 6 — HTML Generation (Worker 3)

Run Worker 3 from lp-builder-agent skill.
- Input: QA-approved (or force-passed) content_blueprint.json
- Output: ./output/[brand_slug]/[brand-slug]-[lp-type]-lp.html
- All HTML wrapped in <div class="claude-lp-wrapper"> with fully scoped CSS

---

### Step 7 — Output Report

Save final file to: production_artifacts/[brand_slug]/[brand-slug]-[lp-type]-lp.html

Print this report:

LP BUILD COMPLETE
─────────────────────────────────
Brand:       [brand_name]
LP Type:     [lp_type]
Output:      production_artifacts/[brand_slug]/[brand-slug]-[lp-type]-lp.html
Primary KW:  [target_keyword]
Keywords:    [count] — [list joined by " · "]
QA Result:   [PASS / FORCE-PASSED after N attempts]
─────────────────────────────────
BROWSER QA (after pasting into WordPress):
□ Reveal button → brand site opens in new tab
□ Coupon code shows, copy button works
□ Mobile: no overflow, buttons tappable
□ Urgency bar: amber = expiry, gray = evergreen
□ FTC disclosure visible in footer
□ No "[" placeholder text on page
─────────────────────────────────
DEPLOY QA (before connecting Google Ads):
□ Affiliate link tested incognito → correct merchant + cookie fires
□ UTM params on all outbound links
□ GA4 coupon_reveal event fires
□ PageSpeed mobile score ≥70
□ Read LP aloud — keywords sound natural
─────────────────────────────────

---

## Rules of Engagement

- Each step's JSON output is the next step's input — never skip a handoff
- Intermediate JSON → output/[brand_slug]/  |  Final HTML → production_artifacts/[brand_slug]/
- Only 1 approval gate: missing competitor_brand on comparison LP
- QA retry max 3 attempts → force-pass with documented issues if still failing
- Every flag, skip, or force-pass must appear in the output report — no silent failures

---

## Full-Funnel Mode

If user says "LP + PPC", "full funnel", or "build everything":
1. Complete all Steps 1–7 above
2. Pass output HTML path as landing_page_url → invoke workflow /build-ppc