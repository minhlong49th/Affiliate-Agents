# Reference 09 — Multi-Brand Batch Workflow
## Scale from 1 brand to 60+ brands/quarter with consistent quality

---

## Overview

The batch workflow allows processing multiple brands in a single session,
applying the full 7-step pipeline to each brand sequentially.
Built for the ProductInsight target of 60+ brands applied/month.

---

## Batch Input Format

Provide brands as a structured list. Minimum required per brand:

```
BATCH:
1. URL: https://brand1.com/affiliate-landing   Platform: both   AG type: auto
2. URL: https://brand2.com                     Platform: google  AG type: coupon
3. URL: https://brand3.com/products            Platform: bing    AG type: review
```

Or as a table:
| # | LP URL | Platform | AG Type | Notes |
|---|--------|----------|---------|-------|
| 1 | https://buildasoil.com | both | auto | Existing winner |
| 2 | https://brand2.com | google | coupon | New brand test |
| 3 | https://brand3.com | bing | review | Bing-first test |

---

## Batch Processing Rules

### Order of operations per brand
1. LP fetch + brand research (Prompt 01)
2. HS-1 hard stop check → if STOP: log, skip to next brand
3. Ad group type selection (Prompt 02)
4. Keyword generation (Prompt 03)
5. Negative keyword generation (Prompt 06)
6. RSA headline generation (Prompt 04)
7. RSA description generation (Prompt 05)
8. QA compliance check (Prompt 07) — auto-fix max 3 attempts
9. CSV export (Prompt 08)
10. Save files + log completion

### Error handling
- LP unreachable → attempt Google cache → if both fail → log "LP UNAVAILABLE" + skip
- HS-1 HARD STOP → log "PPC POLICY VIOLATION: [reason]" + skip
- QA fails after 3 attempts → flag asset as [MANUAL REVIEW] + continue (never block output)
- CSV generation error → output markdown table fallback instead

### Session limits (practical)
- Recommended batch size: 5–10 brands per session
- For 20+ brands: split into multiple sessions
- Heavy LP fetching can timeout — consider staggering

---

## Batch Output Structure

For a batch of N brands, generate:

```
/outputs/
├── _batch-summary.md              ← Overview of all brands processed
├── brand1/
│   ├── brand1-campaign-brief.md
│   ├── brand1-google-ads-import.csv
│   └── brand1-bing-ads-import.csv
├── brand2/
│   ├── brand2-campaign-brief.md
│   └── brand2-google-ads-import.csv
└── SKIPPED-brands.md              ← List of skipped brands + reasons
```

---

## Batch Summary Template

```markdown
# Batch Campaign Generation Summary
Date: [date]
Brands requested: [N]
Brands processed: [X]
Brands skipped: [Y]

## Results by Brand

| Brand | Status | AG1 | AG2 | Keywords | QA Issues | Files |
|-------|--------|-----|-----|----------|-----------|-------|
| BuildASoil | ✅ Complete | ✅ | ✅ | 24 | 0 | 3 files |
| Brand2 | ✅ Complete | ✅ | — | 13 | 1 flagged | 2 files |
| Brand3 | ⛔ Skipped | — | — | — | HS-1 violation | — |

## Skipped Brands
| Brand | Reason | Action |
|-------|--------|--------|
| Brand3 | PPC prohibited in affiliate terms | Contact AM to confirm policy |

## QA Flags Requiring Manual Review
| Brand | Asset | Issue |
|-------|-------|-------|
| Brand2 | H7 | Could not trim below 30 chars after 3 attempts |

## Import Instructions (applies to all)
1. Google: Use Google Ads Editor → Import each brand's CSV separately
2. Bing: Use Microsoft Ads Editor → Import structure CSV; enter RSA headlines manually
3. Pin H1 to Position 1 and H2 to Position 2 after import in both platforms
4. Load all negative keywords to Shared Library before linking to campaigns
5. Apply Kill/Scale check on Day 5 for each campaign
```

---

## Weekly Brand Research Cadence (from ProductInsight OKR system)

To hit 60+ brands applied per month, run batches on this schedule:

### Monday — Research & Qualify batch
- Input: 15–20 brand URLs discovered from UpPromote/GoAffPro/ShareASale browsing
- Run batch through HS-1 check and AG type selection only (skip ad copy)
- Output: qualifying_brands_[week].md with approved list
- Apply brands that pass

### Tuesday → Thursday — Campaign generation batch
- Input: approved brands from Monday (expect 8–12 after HS-1 filtering)
- Run full 7-step pipeline per brand
- Output: all CSVs for Google Ads Editor import
- Import batch into Google Ads Editor

### Friday — Kill/Scale + Pipeline health
- Run Kill/Scale Analysis (Prompt 10) on all campaigns older than 5 days
- Replenish killed campaign slots with new brands from qualifying list
- Update Brand Pipeline Tracker in ClickUp

---

## Reusable Asset Library (build over time)

As you run batches, save high-performing assets for reuse:

### Winning headline patterns (update weekly)
```
HEADLINE PATTERN LIBRARY
========================
Pattern: "[Brand] Coupon Code [Year]"         CTR avg: X%  — KEEP
Pattern: "Save Up to [X]% Off Today"          CTR avg: X%  — KEEP
Pattern: "Verified [Brand] Promo Code"        CTR avg: X%  — KEEP
Pattern: "[Brand] Deals Updated Daily"        CTR avg: X%  — TEST
Pattern: "Code May Expire Anytime"            CTR avg: X%  — LOW
```

### Winning description formulas (update monthly)
```
DESCRIPTION TEMPLATE — HIGH PERFORMER
D2 template: "Reveal your [Brand] coupon and save [X]%–[Y]% on [product]. No signup."
Avg QS contribution: positive (keep this structure for new brands)
```

### Negative keyword additions (running list)
Keep a master text file updated from weekly Search Terms reviews.
Add new junk terms discovered → apply retroactively to all active campaigns.
