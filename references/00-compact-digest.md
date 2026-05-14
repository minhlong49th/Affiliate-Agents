# PPC Campaign Compact Digest
## Complete reference for single-brand pipeline — Steps 1–7

---

### SECTION A — Brand Research Checklist (Step 1)
Extract from landing page:
1. Brand identity (Name, Root domain, Geography)
2. Products & Pricing (Top 3 products, Price points, AOV)
3. Active offers (Coupons, %, free shipping, guarantees)
4. USPs & Positioning (Pain points solved, audience, unique features)
5. Social proof (Reviews, ratings, credentials)
6. Affiliate Program (Check footer for affiliate terms page) -> MUST check PPC Policy (HS-1).
7. Compliance (Privacy policy, Contact page, Affiliate disclosure)

---

### SECTION B — AG Selection Matrix (Step 2)
| Ad Group Type | Primary Strategy | Keyword Indicators |
|---|---|---|
| AG1: Coupon Intent | Joey Babineau (PSBCU) | coupon, promo, discount, deal, save |
| AG2: Product/Review | Hybrid (PSBCU + Crestani) | review, legit, vs, [product name], buy |
| AG3: Problem-Aware | John Crestani (17-step full) | how to, why, what is, struggle |
| AG4: Solution-Aware | John Crestani (comparative) | best, top, vs, compare, ranked |
*Note: For new brands (<1k searches), use AG1 only. Established (>5k searches), use AG1+AG2.*

---

### SECTION C — Keyword Templates AG1 + AG2 (Step 3)
Generate exactly 10-15 highly relevant keywords per AG (Phrase match mostly, Top 3 Exact match).
**AG1 Pattern:** `[Brand] coupon`, `[Brand] discount code`, `[Brand] promo code`, `[Brand] coupon [year]`
**AG2 Pattern:** `[Brand] review`, `is [Brand] legit`, `[Brand] vs [Competitor]`, `[Brand] [Product] reviews`

---

### SECTION D — Negative Keyword Master List (Step 4)
**Tier 1 (Account - Broad Match):** free, jobs, career, hiring, DIY, tutorial, wikipedia, what is, reddit, ebay, amazon, craigslist, scam, lawsuit, side effects, certification
**Tier 2 (Campaign - Phrase Match):** [competitors], wholesale, B2B, for business
**Tier 3 (Ad Group):** AG1 blocks: review, vs, honest opinion. AG2 blocks: coupon code, promo code.

---

### SECTION E — RSA Slot Assignment (Step 5)
| PSBCU Element | RSA slot | AG1 Weight | AG2 Weight |
|---|---|---|---|
| P — Problem | H2–H3, D1 opening | Low (0-1) | Medium (2-3) |
| S — Solution | H3–H5 | "Coupon available" | "Honest review test" |
| B — Benefit | H6–H9, D2 | "Save X%" | "Proven results" |
| C — Call to Action | H10–H12, D3 | "Reveal Code" | "Read Comparison" |
| U — Urgency | H13–H15, D4 | "Ends Soon" | "Price may change" |

---

### SECTION F — RSA Templates AG1 + AG2 (Step 5)
*Mandatory format: H[N] [PIN]: "[text]" | chars=[X] | [PASS/FAIL]*
*Limits: Headlines <= 30 chars. Descriptions <= 90 chars.*

**AG1 Coupon:**
- H1 [PIN 1]: `[Brand] Coupon Code [Year]`
- H2 [PIN 2]: `Save Up to [X]% Off Today`
- H3-H15: [Brand] Deals Today, Free Shipping + [X]% Off, Limited Time Offer, Verified [Brand] Promo Code. No "Official"!
- D1-D4: Problem+Solution, Benefit+CTA+Urgency, Social Proof+Offer, Objection+Final CTA.

**AG2 Review:**
- H1 [PIN 1]: `[Brand] Review [Year]`
- H2 [PIN 2]: `Is [Brand] Worth It?`
- H3-H15: Real Customer Results, See Pros & Cons, [Brand] vs Competitors, Read Before Buying.
- D1-D4: Context+Methodology, Top features+Differentiator, Details+Social Proof, Risk Removal+CTA.

---

### SECTION G — Policy QA Rules (Step 6)
- **A. Limits:** H:30, D:90, Paths:15.
- **B. Caps:** No ALL CAPS except acronyms/coupons.
- **C. Punctuation:** NO "!" in headlines. Max 1 "!" per description. No emojis.
- **D. Language:** No clickbait ("Shocking secret" -> "Discover"). No misspellings.
- **E. Repetition:** No duplicated headlines or phrases.
- **F. Compliance (CRITICAL):**
  - NO "Official Site". Flag any "Official" word as FAIL.
  - No implied brand ownership. Limit superlatives unless proven.
  - No "Click Here" CTA (especially Bing). Use "Reveal Now".
  - MUST match LP offer.

---

### SECTION H — Output Format Specs (Step 7)
Output human-readable markdown + bulk CSV payload.
- Google Ads CSV Headers: Campaign, Ad Group, Keyword, Match Type, Headline 1, Headline 2, etc. (Editor format).
- Bing CSV Headers: Campaign, Ad Group, Keyword, Match type, Title Part 1, Title Part 2, etc. (Bulk Upload format).
Include negatives and extensions in the CSV structure or note them clearly.

---

### SECTION I — Extensions Quick Reference (Step 5.5)
Generate 6 Sitelinks, 6 Callouts, 1 Structured Snippet per Campaign/AG.
- **Sitelinks (Title 25c, D1/D2 35c):** E.g. Reveal Coupon Code, Best Sellers, Review. *MUST verify URL against LP! Output `⚠️ URL NOT VERIFIED` if placeholder.*
- **Callouts (25c):** Verified Coupon Codes, Tested by Real Buyers, No Signup Required.
- **Structured Snippets:** Header: "Products" or "Brands". List >= 6 items.
