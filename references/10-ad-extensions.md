# Reference 10 — Ad Extensions Knowledge File
## Sitelinks · Callout Extensions · Structured Snippets
### Google Ads + Microsoft Ads (Bing) — Affiliate Coupon & Review Model

---

## WHY EXTENSIONS MATTER FOR AFFILIATE CAMPAIGNS

Extensions increase ad real estate by 2–3x on desktop without additional CPC cost.
For coupon/review campaigns specifically:
- Sitelinks let users jump directly to specific product pages or coupon pages
- Callouts reinforce trust signals that can't fit in 30-char headlines
- Structured Snippets showcase product range without wasting RSA space
- Combined: CTR lifts of 10–20% are typical when all 3 types are active

**Extensions do NOT increase cost per click — they only improve CTR and Quality Score.**

---

## SECTION 1 — SITELINKS

### Character Limits

| Field | Google Ads | Microsoft Ads (Bing) |
|---|---|---|
| Sitelink title | 25 chars | 25 chars |
| Description line 1 | 35 chars | 35 chars |
| Description line 2 | 35 chars | 35 chars |
| Min sitelinks to create | 2 | 2 |
| Max sitelinks per campaign | 20 | 20 |
| Shown per ad | 2–6 | 2–4 |

### Rules
- Title must be distinct from other sitelinks (no near-duplicates)
- Each sitelink must point to a different URL on the same domain
- No "Click here" titles (Bing) — must be descriptive
- No exclamation marks in titles
- Descriptions optional but strongly recommended — add when space allows
- Each sitelink URL must be functional and match title content

### ⚠️ SITELINK URL VALIDATION (REQUIRED)

Before finalizing any sitelink URL:
1. Use only paths that VERIFIABLY EXIST on the domain (extracted from LP fetch in Step 1)
2. If a path cannot be confirmed from LP data → use root domain `/` and add note:
   `[SL URL: PLACEHOLDER — verify path exists before launch]`
3. NEVER fabricate URL paths (e.g., `/brand-review` if that page was not found in Step 1)
4. Flag all unverified URLs in Extensions QA output with: `⚠️ URL NOT VERIFIED`

### Sitelink Strategy for Affiliate Coupon Model

**For AG1 — Coupon Intent (6 sitelinks):**

| # | Title (max 25 chars) | D1 (max 35 chars) | D2 (max 35 chars) | URL path |
|---|---|---|---|---|
| SL1 | Reveal Coupon Code | Click to show your discount code | Updated and verified today | /go/[brand] |
| SL2 | [Brand] Best Sellers | Top products with biggest savings | Free shipping on qualifying orders | /go/[brand] |
| SL3 | [X]% Off Sale Items | All active sale items listed here | Prices updated daily | /go/[brand] |
| SL4 | Free Shipping Deals | Orders qualifying for free shipping | [Brand]'s current shipping policy | /go/[brand] |
| SL5 | [Brand] Review | Our honest [brand] product review | Tested by real customers in 2025 | /[brand]-review |
| SL6 | Compare [Brand] | [Brand] vs top competitors ranked | Find the best option for you | /[brand]-review |

**For AG2 — Review Intent (6 sitelinks):**

| # | Title (max 25 chars) | D1 (max 35 chars) | D2 (max 35 chars) | URL path |
|---|---|---|---|---|
| SL1 | [Brand] Full Review | Tested over 30 days – real results | No affiliate bias in our testing | /[brand]-review |
| SL2 | [Brand] vs [Competitor] | Side-by-side product comparison | Which one wins? See our verdict | /[brand]-review |
| SL3 | Pros and Cons | What we love and what we don't | Honest breakdown inside | /[brand]-review |
| SL4 | Best Price + Coupon | Find today's lowest [brand] price | Verified coupon code included | /go/[brand] |
| SL5 | [Top Product] Review | Deep dive into [brand's top product] | Full specs, results, verdict | /[brand]-review |
| SL6 | Who Should Buy It | Is [brand] right for your needs? | Our recommendation by use case | /[brand]-review |

### Sitelink Generation Rules
- Generate 6 sitelinks per ad group (Google shows best-performing 2–6 dynamically)
- If both AG1 and AG2 exist: cross-link between them (coupon → review, review → coupon)
- All sitelinks must point to productinsight.store domain — never direct to brand domain
- Titles: Title Case, no exclamation, no ALL CAPS
- Fill BOTH description lines — ads with descriptions get more real estate

---

## SECTION 2 — CALLOUT EXTENSIONS

### Character Limits

| Field | Google Ads | Microsoft Ads |
|---|---|---|
| Callout text | 25 chars | 25 chars |
| Min to create | 2 | 2 |
| Max per campaign | 20 | 20 |
| Shown per ad | 2–6 | 2–4 |

### Rules
- No punctuation at end of callout (no period, no exclamation)
- No duplicate callouts within same campaign
- No "Click here" phrasing
- Must be factual — not opinion or unsubstantiated superlatives
- Fragment format (not full sentences) — e.g. "Free Shipping Available" not "We offer free shipping"

### Callout Library for Affiliate Coupon/Review Model

**Trust & Credibility callouts:**
```
Verified Coupon Codes        (24 chars)
Updated Daily                (13 chars)
Tested by Real Buyers        (21 chars)
No Signup Required           (20 chars)
100% Free to Use             (16 chars)
Honest Unbiased Reviews      (24 chars)
All Codes Hand-Tested        (22 chars)
Real User Results Inside      (25 chars)
Independent Review Site      (24 chars)
```

**Offer/Value callouts:**
```
Save 5% to 22% Off           (21 chars)
Free Shipping Available      (24 chars)
Multiple Codes Available     (25 chars)
Best Price Guarantee         (22 chars)
Exclusive Discount Codes     (25 chars)
Price Comparison Included    (25 chars)
Latest Deals Listed          (21 chars)
Working Codes Only           (19 chars)
```

**Product/Brand callouts:**
```
Organic USDA Certified       (24 chars)
US-Based Company             (16 chars)
Ships Nationwide             (16 chars)
Award-Winning Formula        (22 chars)
30-Day Satisfaction Policy   (25 chars — check brand guarantee)
Eco-Friendly Products        (22 chars)
```

### Callout Selection Logic

**AG1 Coupon Intent — select 6 from:**
Priority 1 (always include): Verified Coupon Codes, Updated Daily, No Signup Required
Priority 2 (pick 2): Save 5% to 22% Off, Working Codes Only, Multiple Codes Available
Priority 3 (pick 1): US-Based Company, Ships Nationwide, Award-Winning Formula

**AG2 Review Intent — select 6 from:**
Priority 1 (always include): Honest Unbiased Reviews, Tested by Real Buyers, Independent Review Site
Priority 2 (pick 2): Real User Results Inside, Price Comparison Included, All Codes Hand-Tested
Priority 3 (pick 1): 30-Day Satisfaction Policy, Award-Winning Formula, Eco-Friendly Products

---

## SECTION 3 — STRUCTURED SNIPPETS

### Character Limits

| Field | Google Ads | Microsoft Ads |
|---|---|---|
| Header (predefined) | Select from list | Select from list |
| Value (per item) | 25 chars each | 25 chars each |
| Min values | 3 | 3 |
| Max values | 10 | 10 |
| Shown per ad | 3–10 values | 3–6 values |

### Available Header Types (use most relevant)

| Header | Best for affiliate coupon/review |
|---|---|
| **Brands** | Listing brands covered by the site — NOT this brand's own products |
| **Products** | Specific product lines from the brand being promoted |
| **Services** | Less relevant for physical products |
| **Types** | Types of organic soil, amendment types, etc. |
| **Styles** | Formulation styles (organic, synthetic, living soil, etc.) |
| **Models** | Specific product models or recipes |
| **Amenities** | Not typically relevant |
| **Courses** | Not relevant for coupon sites |
| **Featured Hotels** | Not relevant |
| **Degree Programs** | Not relevant |
| **Insurance Coverage** | Not relevant |
| **Neighborhoods** | Not relevant |

### Recommended header selection for affiliate campaigns:

**For Coupon Sites → use "Products" or "Types":**
- Header: Products → lists the specific products available with discounts
- Header: Types → lists categories of products (for broader appeal)

**For Review Sites → use "Brands" or "Models":**
- Header: Brands → lists brands being compared on the page
- Header: Models → lists specific product models reviewed

### Structured Snippet Templates

**Template A — Products (for coupon AG1):**
```
Header: Products
Values (generate from LP product data):
- Potting Soil 3.0          (16 chars)
- Coots Mix Blend           (15 chars)
- Light Recipe Soil         (17 chars)
- Ultra Clean Recipe        (19 chars)
- BuildASoil Amendments     (22 chars)
- Soil Conditioner Kit      (21 chars)
[add up to 10, each ≤25 chars]
```

**Template B — Types (for coupon AG1 alternative):**
```
Header: Types
Values:
- Organic Potting Soil      (20 chars)
- Living Soil Amendments    (24 chars)
- No-Till Garden Blends     (22 chars)
- Compost Amendments        (19 chars)
- Worm Castings             (14 chars)
- Mycorrhizal Inoculants    (24 chars)
```

**Template C — Brands (for review AG2 — comparison pages):**
```
Header: Brands
Values (brand + top competitor):
- BuildASoil                (11 chars)
- Fox Farm                  (8 chars)
- Roots Organics            (15 chars)
- Nature's Living Soil      (21 chars)
- Dr. Earth                 (8 chars)
- California Super Soil     (22 chars)
```

**Template D — Models (for review AG2 — specific product):**
```
Header: Models (or use "Products" if Models not available for category)
Values:
- Potting Soil Recipe 3.0   (23 chars)
- Coots Mix Standard        (19 chars)
- Light Recipe Soil         (17 chars)
- Ultra Clean Commercial    (22 chars)
- BuildASoil Starter Kit    (24 chars)
- Amendments Bundle         (18 chars)
```

### Structured Snippet Rules
- Values must be real — no fabricated product names
- Each value ≤ 25 chars
- Minimum 3 values (Google may not show snippet with fewer)
- List at least 6 values — Google picks best 3–10 dynamically
- No punctuation at end of values
- No "and" or "or" connectors — plain nouns only
- For "Products" header: use actual product names from LP analysis (Step 1)
- For "Brands" header: only list brands with LP content to back them up

---

## SECTION 4 — EXTENSION QA CHECKLIST

Run on every extension before output.

### Sitelink QA
- [ ] Title ≤ 25 chars
- [ ] D1 ≤ 35 chars, D2 ≤ 35 chars
- [ ] No exclamation in title
- [ ] No "Click here" in title
- [ ] URL is on same domain as Final URL
- [ ] URL is functional (not 404)
- [ ] Each sitelink points to a different URL
- [ ] Title is meaningfully different from other sitelinks

### Callout QA
- [ ] Text ≤ 25 chars
- [ ] No period or exclamation at end
- [ ] Factual claim (no unsubstantiated superlatives)
- [ ] No duplicate callouts in same campaign
- [ ] No "Click here" phrasing

### Structured Snippet QA
- [ ] Header selected from Google/Bing approved list
- [ ] Each value ≤ 25 chars
- [ ] Minimum 3 values (6+ recommended)
- [ ] No punctuation at end of values
- [ ] Product names match actual LP content
- [ ] Brand names in "Brands" header have corresponding LP content

---

## SECTION 5 — PLATFORM DIFFERENCES FOR EXTENSIONS

| Feature | Google Ads | Microsoft Ads (Bing) |
|---|---|---|
| Sitelink descriptions | Optional but recommended | Optional but recommended |
| Extension scheduling | Supported (by day/hour) | Supported |
| Extension-level reporting | Full asset reporting | Limited |
| Callout minimum | 2 | 2 |
| Structured snippet headers | Larger predefined list | Same predefined list |
| Auto-extensions | Google may add automatically | Microsoft may add automatically |
| Extension rotation | Optimized automatically | Optimized automatically |

**Bing-specific notes:**
- Sitelinks on Bing tend to show more frequently than on Google for branded searches
- Microsoft Ads calls them "Sitelink Extensions" (not just "Sitelinks") in their UI
- Callouts are called "Callout Extensions" — same rules apply
- Structured Snippets same format — import from Google Ads Editor works via copy-paste

---

## SECTION 6 — CSV FORMAT FOR EXTENSIONS

### Google Ads Editor — Sitelinks
```csv
Campaign,Action,Sitelink Text,Description Line 1,Description Line 2,Final URL,Mobile Final URL,Tracking Template,Start Date,End Date
[Campaign Name],Add,[title],[D1],[D2],[url],,,,
```

### Google Ads Editor — Callouts
```csv
Campaign,Action,Callout Text,Start Date,End Date,Device Preference
[Campaign Name],Add,[callout text],,, All
```

### Google Ads Editor — Structured Snippets
```csv
Campaign,Action,Header,Values,Start Date,End Date,Device Preference
[Campaign Name],Add,[Header Type],"[value1]; [value2]; [value3]; [value4]; [value5]; [value6]",,,All
```

### Microsoft Ads Bulk — Sitelink Extensions
```csv
Type,Status,Campaign,Ad Group,Sitelink Extension Text,Description 1,Description 2,Final URL
Sitelink Extension,Active,[Campaign],,[ title],[D1],[D2],[url]
```

### Microsoft Ads Bulk — Callout Extensions
```csv
Type,Status,Campaign,Ad Group,Callout Text
Callout Extension,Active,[Campaign],,[callout text]
```

### Microsoft Ads Bulk — Structured Snippet Extensions
```csv
Type,Status,Campaign,Ad Group,Structured Snippet Header,Structured Snippet Values
Structured Snippet Extension,Active,[Campaign],,"[Header]","[v1]; [v2]; [v3]; [v4]; [v5]; [v6]"
```
