# Reference 02 — Ad Group Strategy Decision Tree
## Joey Babineau × John Crestani Combined Framework

---

## Step A: Auto-detect ad group type (if not specified by user)

Run this decision tree using data from Step 1 (brand research) and provided keyword list.

```
Has keyword list?
├── YES → Classify each keyword → assign to ad group type (see Section 1)
└── NO → Infer from LP content → see Section 2
```

---

## Section 1: Keyword-based Classification

Classify each keyword from the provided list into one of 4 intent types:

| Keyword signal words | Ad Group Type | Primary Strategy |
|---|---|---|
| coupon, promo code, discount code, voucher, code, save | **AG1 — Coupon Intent** | Joey Babineau |
| review, reviews, legit, worth it, honest, scam or not, vs, compare, alternative | **AG2 — Product/Review Intent** | Joey + Crestani hybrid |
| how to, why, problem, help, solution, tips, struggling | **AG3 — Problem-Aware** | John Crestani |
| best, top, recommended, vs [category], [category] review | **AG4 — Solution-Aware** | John Crestani |

If a keyword doesn't fit any group → default to AG2 (most flexible).

Create one ad group per type that has at least 2 keywords. Minimum 1 ad group total.

---

## Section 2: LP Content-based Auto-selection

If no keywords provided, select ad group types based on LP characteristics:

| LP characteristic | Recommended ad groups to create |
|---|---|
| Has active coupon/discount visible | AG1 (Coupon) — always create |
| Has detailed product description | AG2 (Product/Review) — create |
| AOV > $80 AND product is complex | AG2 + AG4 (Solution-Aware) |
| Brand search volume < 1,000/mo (small brand) | AG1 only — lowest CPC risk |
| Brand is well-known (> 10,000/mo) | AG1 + AG2 |
| No coupon found on LP | AG2 only (review/informational angle) |

Default auto-generated keyword sets per ag type: see Reference 03.

---

## Section 3: Strategy Configuration per Ad Group Type

### AG1 — Coupon Intent
**Lead strategy:** Joey Babineau — PSBCU framework, branded transactional

- Keyword pattern: `[brand] coupon`, `[brand] promo code`, `[brand] discount`
- Match type: Phrase Match
- LP type: Coupon reveal page (existing LP)
- Bid guidance: Start low ($0.30–0.60 target CPC) — these convert at 3–5%
- Budget: Include in Shared Budget batch if testing
- PSBCU distribution: P=0, S=2, B=4, C=4, U=3, remaining=fill with brand variations

### AG2 — Product/Review Intent
**Lead strategy:** Joey + Crestani hybrid

- Keyword pattern: `[brand] review`, `[brand] vs [competitor]`, `buy [brand]`
- Match type: Phrase Match
- LP type: Review/comparison page
- Bid guidance: $0.40–0.90 target CPC
- PSBCU distribution: P=2, S=3, B=3, C=3, U=2, remaining=social proof
- Supplement with Crestani 17-step steps 1–7 for description copy

### AG3 — Problem-Aware
**Lead strategy:** John Crestani — full funnel, broad intent

- Keyword pattern: `how to [solve problem]`, `[problem] help`, `[problem] solution`
- Match type: Broad Match → narrow to Phrase after 2 weeks data
- LP type: Advertorial/story-style LP (may need new LP build)
- Bid guidance: $0.30–1.00 CPC — higher volume, lower CVR
- 17-step application: Steps 1–4 in headlines, Steps 5–8 in descriptions

### AG4 — Solution-Aware
**Lead strategy:** John Crestani — mid-funnel comparison

- Keyword pattern: `best [category]`, `top [product type]`, `[brand] vs [competitor]`
- Match type: Phrase Match
- LP type: Comparison/review LP
- Bid guidance: $0.80–2.50 CPC
- 17-step application: Steps 4–9 in headlines, Steps 10–14 in descriptions

---

## Section 4: Ad Group Naming Convention

```
[Brand] | [Type] | [Platform] | [Year]

Examples:
BuildASoil | Coupon | Google | 2025
BuildASoil | Review | Bing | 2025
BuildASoil | Problem | Google | 2025
```

---

## Section 5: Campaign-level Settings

### Google Ads
- Campaign type: Search
- Network: Search only (disable Search Partners and Display Network)
- Bidding: Manual CPC (test phase) → Maximize Conversions after 30+ conv/month
- Budget: Use Shared Budget during batch testing ($5/day per campaign in batch)
- Location: Tier 1 countries (US, UK, CA, AU, NZ) — target "People IN this location"
- Language: English
- Ad rotation: Optimize (let Google test combinations)
- Conversion tracking: Confirm coupon_reveal event is set up before launching

### Microsoft Ads (Bing)
- Campaign type: Search
- Network: Bing ONLY — disable Search Partners (manual exclusion after setup)
- Bidding: Manual CPC — CPC target 20–30% lower than Google equivalent
- Budget: Lower than Google during test phase (Bing = validation platform)
- Audience Network: MUST exclude manually post-setup (add to exclusion lists)
- Location: Same Tier 1 targets as Google
- Ad scheduling: Same as Google for consistency
