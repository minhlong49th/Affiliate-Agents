# Reference 01 — LP Analysis Protocol

## Purpose
Standardized protocol for fetching, reading, and extracting structured data from an affiliate
landing page URL before any ad copy generation begins.

---

## Fetch Protocol

1. Use web_fetch tool on the provided `landing_page_url`.
2. If fetch fails (403, timeout, Cloudflare block) → attempt Google cache version:
   `https://webcache.googleusercontent.com/search?q=cache:[URL]`
3. If both fail → ask user to paste LP content manually.

---

## Step 1b — Affiliate Program PPC Policy Deep Check

After fetching the main LP, scan the page footer for links containing:
"affiliate", "partner", "program", "terms", "earn", "refer"

If found:
1. Note the affiliate program page URL
2. Fetch that page separately
3. Re-run PPC Policy check (Section: HS-1) on the affiliate terms content
4. Override LP-based classification only if affiliate terms are more restrictive

**Rule:** Do NOT classify as CLEAR based on LP alone if an affiliate terms link exists and was not fetched.
Classification logic stays the same — but input must include both LP + affiliate terms.

---

## Extraction Checklist

After fetching, extract and structure the following. Mark as [NOT FOUND] if absent.

### A — Brand & Identity
- [ ] Brand name (exact spelling and capitalization)
- [ ] Brand domain / root domain
- [ ] Tagline or brand positioning statement
- [ ] Geographic market (US only? Tier 1? Global?)

### B — Products & Offers
- [ ] Top 3 product names (exact names for keyword use)
- [ ] Price points (or price range)
- [ ] Active coupon codes (if any — note if evergreen or seasonal)
- [ ] Discount percentage or amount being offered
- [ ] Shipping terms (free shipping threshold, regions)
- [ ] Money-back guarantee (if any, duration)

### C — Audience & Intent Signals
- [ ] Who is this product for? (explicit audience mentions)
- [ ] Pain points or problems the product solves
- [ ] Key benefits / USPs mentioned
- [ ] Comparison language (better than X, vs Y)

### D — Trust & Social Proof
- [ ] Number of reviews / rating mentioned
- [ ] Named awards, certifications, press mentions
- [ ] User testimonials (count and sentiment)
- [ ] Founded date / years in business

### E — Affiliate & Policy
- [ ] Affiliate disclosure present? (required — note location: top/footer/none)
- [ ] Affiliate network (UpPromote, GoAffPro, ShareASale, CJ, Impact, etc.)
- [ ] Commission rate (if visible)
- [ ] PPC policy (search LP and affiliate program page — critical HS-1 check)

### F — Technical & Compliance
- [ ] Page load speed (subjective: fast / slow)
- [ ] Mobile-friendly (yes/no from fetch response)
- [ ] Privacy policy / Terms page linked (yes/no)
- [ ] Contact page present (yes/no)
- [ ] FTC affiliate disclosure (yes/no — required for compliant ad campaign)

---

## PPC Policy Hard Stop Check (HS-1)

Before generating any ad copy, verify:

1. Search LP and affiliate program terms for: "PPC", "paid search", "Google Ads", "brand
   bidding", "trademark", "SEM"
2. Classify result:

| Finding | Decision |
|---------|----------|
| No mention of PPC restrictions | ✅ PROCEED |
| "PPC allowed but not brand name in ad text" | ✅ PROCEED with note — avoid brand name in headlines |
| "No bidding on brand keywords" / "trademark prohibited" | 🛑 HARD STOP — output error message |
| "No paid search of any kind" | 🛑 HARD STOP — output error message |
| Terms not found / ambiguous | ⚠️ FLAG — note in brief as "PPC policy unclear — verify before launching" |

**If HARD STOP:** Output message:
```
⛔ PPC POLICY VIOLATION DETECTED
Brand: [brand name]
Policy found: [exact text]
This brand prohibits PPC bidding on brand terms. Running this campaign risks affiliate account
termination. Campaign generation aborted. Verify with affiliate manager before proceeding.
```

---

## Output Format from Step 1

Produce a structured brand research summary:

```
BRAND RESEARCH SUMMARY
======================
Brand name:        [name]
Domain:            [domain]
Market:            [US/Tier1/Global]
Top products:      [product 1], [product 2], [product 3]
Active coupon:     [code] — [type: evergreen/seasonal/none]
Discount:          [X% off / $X off / free shipping / none found]
Guarantee:         [X-day MBG / none]
USPs:              [bullet list]
Pain points:       [bullet list]
Social proof:      [X reviews, Y stars / none]
Affiliate network: [network name]
PPC policy:        [CLEAR / FLAG / HARD STOP]
Disclosure:        [present at: top/footer / NOT FOUND]
```
