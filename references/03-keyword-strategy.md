# Reference 03 — Keyword Strategy & Generation

---

## Keyword Generation Logic

### IF keywords provided by user:
1. Validate each keyword (not empty, not competitor-brand-only without LP relevance)
2. Classify into intent groups (see Reference 02 Section 1)
3. Add match type: all → Phrase Match by default
4. Flag any keyword with avg CPC likely > $2.00 (based on niche signals) for manual review

### IF no keywords provided:
Auto-generate from brand research data (brand name, top products, competitors found on LP).

---

## Auto-generation Templates

### AG1 — Coupon Intent Keywords (generate all variants)

```
Primary transactional (generate all):
[brand] coupon
[brand] coupon code
[brand] promo code
[brand] promo
[brand] discount
[brand] discount code
[brand] voucher
[brand] code
[brand] sale
[brand] deal
[brand] offer
[brand] free shipping
[brand] savings

With [top product name] (if product known):
[brand] [product] coupon
[brand] [product] discount
[brand] [product] deal
```

### AG2 — Product/Review Intent Keywords (generate all variants)

```
Review intent:
[brand] review
[brand] reviews
[brand] [product] review
is [brand] legit
is [brand] worth it
[brand] honest review
[brand] verified review

Comparison intent (only if competitor found on LP or in niche):
[brand] vs [competitor]
[brand] vs [competitor] review
[brand] alternative
[brand] comparison

Purchase intent:
buy [brand]
[brand] where to buy
[brand] [product] price
[brand] [product] buy online
order [brand] online
```

### AG3 — Problem-Aware Keywords (only if LP supports advertorial content)

```
Use brand's pain point data from LP analysis.
Pattern: [problem verb phrase] / [problem noun + help/solution/tips]

Examples for organic soil niche:
how to improve garden soil
why is my soil compacted
organic garden soil problems
soil amendment help
plants not growing in soil
```

### AG4 — Solution-Aware Keywords

```
Pattern: best/top [category] + comparison terms

Examples for organic soil niche:
best organic potting soil
top organic soil amendments
organic soil that actually works
[brand] vs [competitor] potting soil
[category] review [year]
```

---

## Match Type Assignment

| Intent Group | Default Match Type | Upgrade to Exact when |
|---|---|---|
| AG1 Coupon | Phrase Match | CTR > 5% AND conv > 0 on keyword |
| AG2 Product | Phrase Match | CTR > 3% AND conv > 0 on keyword |
| AG3 Problem | Broad Match → Phrase after 14 days | Has > 5 clicks in 14 days |
| AG4 Solution | Phrase Match | Same as AG2 |

**Format for CSV output:**
- Phrase Match: `"keyword"` (with quotes in CSV)
- Exact Match: `[keyword]` (with brackets in CSV)
- Broad Match: `keyword` (no formatting)

---

## Keyword Volume Guidance (add as notes, not hard stops)

| Estimated monthly volume | Signal | Action |
|---|---|---|
| > 1,000/mo (head term) | Brand has audience | Proceed |
| 50–999/mo (coupon KW) | Normal coupon range | Proceed — this is the target range |
| < 50/mo (coupon KW) | Low volume risk | Flag — note in brief, still include |
| 0/mo (coupon KW) | No search demand | Note "First Mover" risk — include at lower bid |

---

## Keywords to EXCLUDE from generation (auto-filtered)

Never auto-generate these keyword types:
- Generic category terms without brand (e.g., "organic soil" without brand name) — too broad, CPC too high
- Competitor-only keywords (e.g., "fox farm coupon") — different campaign if needed
- Informational pure research keywords without commercial intent (e.g., "what is organic soil")
- Any keyword containing words in the account-level negative list (see Reference 04)

---

## Keyword Output Format

For each generated keyword, output in this structure:

```
Keyword: [keyword text]
Match type: [Phrase/Exact/Broad]
Ad group: [AG1/AG2/AG3/AG4]
Intent: [Transactional/Commercial/Informational]
Est. CPC range: [low-high based on niche signals]
```
