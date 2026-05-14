# Reference 06 — Policy Compliance QA Checklist
## Google Ads + Microsoft Advertising Editorial Standards

---

## QA Protocol

Run this checklist on EVERY generated asset before output.
For each FAIL: auto-fix once. Re-run check. Max 3 auto-fix attempts per asset.
After 3 fails: mark `[MANUAL REVIEW REQUIRED: reason]` and continue to next asset.

Log format per attempt:
```
Asset: [H1 / H2 / D1 / etc.]
Attempt: [1/2/3]
Issue: [rule violated]
Fix applied: [what was changed]
Result: [PASS / FAIL → attempt N]
```

---

## SECTION A — Character Limits (CRITICAL — auto-reject if violated)

| Check | Rule | Auto-fix method |
|---|---|---|
| A1 | Headline ≤ 30 chars | Remove lowest-value word; try abbreviation |
| A2 | Description ≤ 90 chars | Shorten to next sentence boundary; trim filler words |
| A3 | Display path ≤ 15 chars | Truncate to brand slug; remove spaces |
| A4 | Minimum 3 words (Bing) | Add brand name if needed |

**Character counting rule:** Count all characters including spaces, punctuation, numbers.

---

## SECTION B — Capitalization Rules

| Check | Rule | Platform | Auto-fix |
|---|---|---|---|
| B1 | No ALL CAPS words (except acronyms) | Both | Lowercase violating word |
| B2 | No intercapitalization (fReE, Fr33) | Both | Normalize to Title Case |
| B3 | Acronyms allowed: USA, FAQ, LP, CTA, MBG | Both | Keep as-is |
| B4 | Brand name capitalization must match brand | Both | Check brand research data, correct |
| B5 | Coupon codes may be ALL CAPS | Both | Keep as-is |
| B6 | Title Case acceptable (first letter of each word) | Both | Keep as-is |

---

## SECTION C — Punctuation & Symbols

| Check | Rule | Platform | Auto-fix |
|---|---|---|---|
| C1 | No exclamation marks in headlines | Both | Remove ! |
| C2 | Max 1 exclamation mark per description | Both | Remove extra ! |
| C3 | No repeated punctuation (!!!, ???, ...) | Both | Reduce to single mark |
| C4 | No emoji in any asset | Both | Remove emoji entirely |
| C5 | No decorative symbols (★ ♥ ☞ →) | Both | Remove symbol |
| C6 | Standard punctuation OK: . , - / : ; & + $ % ( ) | Both | Keep as-is |
| C7 | Trademark symbols (™ ®) allowed if registered brand | Both | Keep if verified brand |

---

## SECTION D — Language & Style

| Check | Rule | Platform | Auto-fix |
|---|---|---|---|
| D1 | No intentional misspellings (leet speak, text speak) | Both | Correct to standard English |
| D2 | No excessive abbreviations | Both | Spell out |
| D3 | No double spaces | Both | Replace double space with single |
| D4 | No leading or trailing spaces | Both | Trim |
| D5 | No sensational/clickbait language | Both | Replace with factual equivalent |
| D6 | No vague generic phrases ("Buy products here") | Both | Replace with specific copy |
| D7 | No profanity or offensive language | Both | Remove or replace |

### Sensational language blacklist — auto-replace:
```
"You won't believe" → "See why"
"Shocking secret" → "Discover"
"Doctors hate this" → [remove entirely]
"GUARANTEED to work" → "Proven results"
"Never seen before" → "New [product]"
"Warning:" → [remove if not genuine]
```

---

## SECTION E — Repetition

| Check | Rule | Auto-fix |
|---|---|---|
| E1 | No repeated words within same headline | Rephrase |
| E2 | No near-duplicate headlines (>80% same words) | Rewrite one with different PSBCU element |
| E3 | No "free free shipping" style repetition in descriptions | Deduplicate |

---

## SECTION F — Affiliate & Business Compliance (HIGH PRIORITY)

| Check | Rule | Platform | Auto-fix |
|---|---|---|---|
| F1 | No "Official Site" claim | Both | Replace with "[Brand] Coupon & Review" |
| F2 | No implied brand ownership | Both | Add "Affiliate" or remove claim |
| F3 | No "Authorized Dealer" without evidence | Both | Remove if not verified |
| F4 | No phone number in ad text | Both | Remove entirely |
| F5 | No fake scarcity (auto-reset countdown) | Both | Replace with evergreen urgency |
| F6 | No "Click Here" CTA | Bing especially | Replace with specific CTA verb |
| F7 | Ad promise must match LP content | Both | Align to LP data from Step 1 |
| F8 | No unsubstantiated superlatives | Both | Add qualifier or remove |

### F1 examples:
```
FAIL: "BuildASoil Official Store"
FIX:  "BuildASoil Coupon & Review"

FAIL: "Official BuildASoil Coupon"
FIX:  "Verified BuildASoil Coupon"

FAIL: "BuildASoil – Buy Direct"
FIX:  "BuildASoil – Best Price Found"
```

### F1a — Extended "Official" Pattern Check
```
ALSO FAIL (catch these variants):
FAIL: "Official [Brand] Sale"       → FIX: "[Brand] Best Sale"
FAIL: "Official [Brand] Discount"   → FIX: "Verified [Brand] Discount"
FAIL: "Official Promo Code"         → FIX: "Verified Promo Code"
FAIL: "[Brand] – Official Deals"    → FIX: "[Brand] – Verified Deals"
```
Rule: Flag ANY headline containing the word "Official" — no exceptions for affiliates.

### F6 CTA replacement map (Bing):
```
"Click here" → "Reveal Now" / "See Code" / "Get Discount"
"Click to save" → "Unlock Savings"
"Click for coupon" → "Reveal Coupon"
"Visit site" → "See Current Price"
```

---

## SECTION G — Display URL & Landing Page

| Check | Rule | Auto-fix |
|---|---|---|
| G1 | Display URL domain matches Final URL domain | Correct to match |
| G2 | No misleading path (path ≠ actual page topic) | Align path to LP content |
| G3 | LP must be functional (not 404, not under maintenance) | Flag if LP down |
| G4 | LP must contain offer mentioned in ad | Flag if mismatch |
| G5 | LP must have affiliate disclosure | Note in brief; cannot fix in ad |

---

## SECTION H — Platform-Specific Checks

### Google Ads Only
| Check | Rule |
|---|---|
| H-G1 | Business name field = actual site name, no promotional text |
| H-G2 | Ad Strength target: "Good" or "Excellent" (requires 8+ unique headlines) |
| H-G3 | No trademark use implying brand ownership (trademark in path OK) |

### Microsoft Ads (Bing) Only
| Check | Rule |
|---|---|
| H-B1 | Minimum 3 words in every headline and description |
| H-B2 | "Click here" explicitly banned |
| H-B3 | No pop-up instructions embedded in ad text |
| H-B4 | Affiliate "Official Site" explicitly banned (harsher than Google) |

---

## QA Output Format

After running all checks, output for each ad group:

```
QA REPORT — [Campaign Name] / [Ad Group Name]
==============================================
Platform: [Google/Bing/Both]

HEADLINES:
H1: "[text]" — [PASS / FIX applied: reason / MANUAL REVIEW REQUIRED: reason]
H2: "[text]" — [PASS / ...]
...H15

DESCRIPTIONS:
D1: "[text]" — [PASS / ...]
D2: "[text]" — [PASS / ...]
D3: "[text]" — [PASS / ...]
D4: "[text]" — [PASS / ...]

DISPLAY PATH:
Path 1: "[text]" — [PASS / ...]
Path 2: "[text]" — [PASS / ...]

NEGATIVE KEYWORDS: [PASS — X terms, no conflicts found]

OVERALL STATUS: [READY TO EXPORT / PARTIAL — N assets flagged for manual review]
```

---

## SECTION I — Extensions QA (Step 5.5)

Run after generating sitelinks, callouts, and structured snippets.
Same auto-fix protocol: max 3 attempts per asset, then flag for manual review.

### I-1 — Sitelinks QA Rules

| Check | Rule | Platform | Auto-fix |
|---|---|---|---|
| I-1a | Title ≤ 25 chars | Both | Trim to next word boundary |
| I-1b | D1 ≤ 35 chars | Both | Trim to next clause boundary |
| I-1c | D2 ≤ 35 chars | Both | Trim to next clause boundary |
| I-1d | No exclamation in title | Both | Remove ! |
| I-1e | No "Click Here" in title | Bing especially | Replace with specific verb |
| I-1f | URL on same domain as Final URL | Both | Correct domain, keep path |
| I-1g | Each sitelink points to different URL | Both | Adjust path — no duplicate URLs |
| I-1h | Title meaningfully different from other sitelinks | Both | Rewrite with different PSBCU element |
| I-1i | No ALL CAPS in title | Both | Normalize to Title Case |
| I-1j | Sitelink URL must be functional | Both | Flag if URL returns 404 |

### I-2 — Callout QA Rules

| Check | Rule | Auto-fix |
|---|---|---|
| I-2a | Text ≤ 25 chars | Trim to last complete word |
| I-2b | No period at end | Remove period |
| I-2c | No exclamation at end | Remove ! |
| I-2d | No duplicate callouts in same campaign | Rewrite with synonym |
| I-2e | No "Click here" phrasing | Replace with factual claim |
| I-2f | Factual, substantiated claim | Remove or qualify superlatives |
| I-2g | Fragment format — not a full sentence | Remove subject + verb if needed |

### I-3 — Structured Snippet QA Rules

| Check | Rule | Auto-fix |
|---|---|---|
| I-3a | Header from approved Google/Bing list | Select closest matching approved header |
| I-3b | Each value ≤ 25 chars | Trim to last complete word |
| I-3c | Minimum 3 values (6+ recommended) | Add generic category values if LP data sparse |
| I-3d | No end punctuation on values | Remove . , ! from end |
| I-3e | Product names match LP content | Replace invented names with actual LP products |
| I-3f | "Brands" header only with LP-backed brands | Remove brands without LP content |

### I-4 — Extensions QA Output Format

```
EXTENSIONS QA — [Campaign Name]
================================
Platform: [Google/Bing/Both]

SITELINKS ([ad group]):
SL1 "[title]" — [PASS / FIX attempt 1: reason / MANUAL REVIEW]
SL2 "[title]" — [PASS / ...]
SL3 "[title]" — [PASS / ...]
SL4 "[title]" — [PASS / ...]
SL5 "[title]" — [PASS / ...]
SL6 "[title]" — [PASS / ...]

CALLOUTS (campaign-level):
C1 "[text]" — [PASS / FIX: reason]
C2 "[text]" — [PASS / ...]
C3 "[text]" — [PASS / ...]
C4 "[text]" — [PASS / ...]
C5 "[text]" — [PASS / ...]
C6 "[text]" — [PASS / ...]

STRUCTURED SNIPPET:
Header: [type] — [PASS / FIX]
Values: [X]/[X] PASS, [Y] fixed

EXTENSION OVERALL: [READY / PARTIAL — N flagged]
```
