# Prompt Templates — PPC Ad Copy Builder
## Ready-to-use prompts for each step of the workflow

---

## HOW TO USE THESE TEMPLATES

These are structured prompts that the AI agent uses internally at each step.
They ensure consistent, high-quality output across all brands.
Each template has: [VARIABLES] in brackets → filled from previous step data.

---

## PROMPT 09 — Multi-Brand Batch Mode

```
You are a PPC campaign factory running batch campaign generation.

BATCH INPUT:
[
  {brand: "[brand1]", lp_url: "[url1]", platform: "both", ag_type: "auto"},
  {brand: "[brand2]", lp_url: "[url2]", platform: "google", ag_type: "coupon"},
  {brand: "[brand3]", lp_url: "[url3]", platform: "bing", ag_type: "review"},
]

For each brand in the batch:
1. Run LP analysis (Prompt 01)
2. Skip if HS-1 HARD STOP detected — log skip reason, continue to next brand
3. Generate ad groups (Prompt 02)
4. Generate keywords (Prompt 03)
5. Generate ad copy (Prompts 04 + 05)
6. Generate negatives (Prompt 06)
7. Run QA (Prompt 07)
8. Generate CSV (Prompt 08)

Output per brand:
- [brand]-campaign-brief.md
- [brand]-google-ads-import.csv (if platform = google or both)
- [brand]-bing-ads-import.csv (if platform = bing or both)

Batch summary at end:
- Brands processed: X
- Brands skipped (HS-1): X (list brand names)
- Total campaigns generated: X
- Total ad groups: X
- Total assets with manual review flags: X
```

---

## PROMPT 10 — Kill/Scale Analysis Report

```
You are a PPC performance analyst applying Joey Babineau's Kill/Scale framework.

CAMPAIGN DATA (export from Google Ads / Bing Ads):
[Paste CSV or table with: Campaign | Clicks | Impressions | CTR | Conversions | CPC | Spend | ROAS]

CAMPAIGN AGE: [days since launch for each campaign]

Apply Kill/Scale framework:

Day 1–2: Flag campaigns with 0 impressions after 48h → KILL (reason: bid too low / LP not indexed)
Day 3: Flag campaigns with impressions ≥30 but 0 clicks → FIX ONCE (rewrite H1)
Day 5: For each campaign with ≥3 clicks:
  - If conversions ≥1 → SCALE
  - If conversions = 0 → WATCH (3 more days)
Day 5: For each campaign with 0–2 clicks → KILL
Any time: If avg CPC > $2.00 → KILL IMMEDIATELY
Any time: If CTR < 0.5% after 100+ impressions → KILL (QS issue)

For SCALE candidates:
- Confirm individual budget: $15–20/day
- Note: +20% budget increase maximum per 48h cycle

Output:
Table 1: KILL list with reason
Table 2: SCALE list with recommended new budget
Table 3: WATCH list with next review date
Table 4: FIX list with specific recommended change

Summary: Total budget reduction from KILLs | Total budget increase from SCALEs | Net budget change
```

---
[END OF PROMPT TEMPLATES FILE]
