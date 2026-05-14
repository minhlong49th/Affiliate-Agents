# Reference 07 — Output Format Specifications

---

## Output 1: Campaign Brief (Markdown)

Generate a human-readable summary first, before the CSV.

### Template:
```markdown
# PPC Campaign Brief
## [Brand Name] — [Platform] Campaign
Generated: [date]

---

## Brand Summary
- Brand: [name]
- LP URL: [url]
- Active offer: [coupon code / discount % / free shipping / none]
- Platform: [Google / Bing / Both]
- PPC policy: [CLEAR / FLAGGED — see note]

---

## Campaign Structure

### Campaign: [Brand] | [Platform] | [Year]
- Type: Search
- Budget: $[X]/day (Shared Budget recommended for test phase)
- Location: [Tier 1 countries selected]
- Bidding: Manual CPC

#### Ad Group 1: [Brand] | Coupon | [Platform] | [Year]
- Keywords ([X] total — Phrase Match):
  - "[brand] coupon code"
  - "[brand] promo code"
  - [... list all]
- Negative keywords (Ad Group level): [list]

**RSA Ad Copy:**
| Slot | Text | Chars | Pin? | QA |
|------|------|-------|------|-----|
| H1 | BuildASoil Coupon Code 2025 | 28 | PIN P1 | PASS |
| H2 | Save Up to 20% Off Today | 25 | PIN P2 | PASS |
| H3 | Verified BuildASoil Promo Code | 30 | — | PASS |
[... all 15 headlines]

| Slot | Text | Chars | QA |
|------|------|-------|-----|
| D1 | [text] | 88 | PASS |
[... all 4 descriptions]

Display URL: productinsight.store / [Brand] / Coupon

[Repeat for each Ad Group]

---

## Negative Keyword Summary
- Account level ([X] terms): [list]
- Campaign level ([X] terms): [list]
- Ad group level ([X] terms): [list]

---

## QA Summary
- Total assets generated: [X]
- PASS: [X]
- Auto-fixed: [X] (fixes logged above)
- Manual review required: [X] (see flagged items)

---

## Next Steps
1. Import CSV into [platform] using instructions below
2. Set up conversion tracking (coupon_reveal event) before launching
3. Add all negative keywords to Shared Library first
4. Disable Search Partners / Audience Network (Bing)
5. Review after 72h — apply Kill/Scale framework

---

## Import Instructions
### Google Ads: Google Ads Editor → File → Import → CSV
### Bing: Microsoft Advertising Editor → File → Import → From file
```

---

## Output 2: Google Ads Editor CSV Format

Google Ads Editor accepts a specific CSV structure. Every column must be present even if empty.

### Campaign-level row:
```csv
Campaign,Campaign Daily Budget,Campaign Type,Campaign Status,Networks,Languages,Location,Ad Schedule,Device Bid Adjustments
[Campaign Name],[budget],Search,Enabled,Google Search,English,"United States; United Kingdom; Canada; Australia; New Zealand",,
```

### Ad Group-level row:
```csv
Campaign,Ad Group,Ad Group Status,Max CPC
[Campaign Name],[Ad Group Name],Enabled,[cpc]
```

### RSA ad row:
```csv
Campaign,Ad Group,Ad Type,Ad Status,Headline 1,Headline 2,Headline 3,Headline 4,Headline 5,Headline 6,Headline 7,Headline 8,Headline 9,Headline 10,Headline 11,Headline 12,Headline 13,Headline 14,Headline 15,Description 1,Description 2,Description 3,Description 4,Path 1,Path 2,Final URL
[campaign],[ad group],Responsive search ad,Enabled,[h1],[h2],[h3],[h4],[h5],[h6],[h7],[h8],[h9],[h10],[h11],[h12],[h13],[h14],[h15],[d1],[d2],[d3],[d4],[path1],[path2],[final_url]
```

### Keyword row:
```csv
Campaign,Ad Group,Keyword,Match Type,Status,Max CPC,Final URL
[campaign],[ad group],[keyword],Phrase,Enabled,[cpc],[final_url]
```

### Negative keyword row (campaign level):
```csv
Campaign,Ad Group,Keyword,Match Type,Status
[campaign],,free,Broad,Enabled
[campaign],,jobs,Broad,Enabled
```

### Pinned headline notation for Google Ads Editor:
In the CSV, pinning is specified by appending the position to the headline column header:
- Column "Headline 1" = pinned to Position 1 if the ad has pin settings
- Use Editor UI to set pins after import (pins cannot be set via standard CSV)
- Note in brief: "Pin H1 to Position 1 and H2 to Position 2 manually after import"

---

## Output 3: Microsoft Advertising Bulk Upload CSV Format

Microsoft Ads uses a "Type" column to differentiate entity types.

### Headers (must be first row):
```csv
Type,Status,Campaign,Ad Group,Keyword,Match Type,Max CPC,Ad Title,Ad Title Part 2,Ad Title Part 3,Description,Description 2,Display URL,Destination URL,Final URL,Custom Parameter,Mobile Final URL,Path 1,Path 2
```

### Campaign row:
```csv
Campaign,Active,[Campaign Name],,,,,,,,,,,,,,,,,
```

### Ad Group row:
```csv
Ad Group,Active,[Campaign Name],[Ad Group Name],,,,,,,,,,,,,,,,
```

### RSA row (Microsoft Bulk format):
```csv
Responsive Search Ad,Active,[Campaign Name],[Ad Group Name],,,,[H1],[H2],[H3],[D1],[D2],[display_url],[],[final_url],,,,[path1],[path2]
```
*(Note: Microsoft Bulk upload for RSA requires the full JSON-based bulk format for all 15 headlines.
Generate a note in the brief to use Microsoft Ads Editor for RSA import, which handles the full
15-headline structure via the RSA creation wizard.)*

### Keyword row:
```csv
Keyword,Active,[Campaign Name],[Ad Group Name],[keyword],[Phrase/Exact/Broad],[cpc],,,,,,,,[final_url],,,,
```

### Negative keyword — Campaign level:
```csv
Campaign Negative Keyword,Active,[Campaign Name],,[keyword],[Broad/Phrase/Exact],,,,,,,,,,,,,,
```

### Negative keyword — Ad Group level:
```csv
Ad Group Negative Keyword,Active,[Campaign Name],[Ad Group Name],[keyword],[Exact],,,,,,,,,,,,,,
```

---

## File Naming Convention

```
[brand-slug]-google-ads-import.csv
[brand-slug]-bing-ads-import.csv
[brand-slug]-campaign-brief.md

Examples:
buildasoil-google-ads-import.csv
buildasoil-bing-ads-import.csv
buildasoil-campaign-brief.md
```

---

## Important Notes for Bing CSV

1. Microsoft Ads Editor is REQUIRED for importing RSAs with all 15 headlines — the bulk CSV only
   supports up to 3 headlines for text ads. RSA content must be entered via Editor UI or API.
   Include this note prominently in campaign brief.

2. After import, immediately:
   - Go to Campaign Settings → Uncheck "Search Partners"
   - Go to Campaign Settings → Audience Network exclusion list → add junk domains
   - Add all negative keywords to Shared Library first, then apply to campaign

3. Bing-specific bid adjustment: set all initial bids 20–30% lower than Google equivalents
   (Bing CPC typically lower for same keywords).

---

## Output 4: Extensions in Google Ads Editor CSV

Extensions are appended to the same CSV as campaigns/ad groups/keywords.
Add these rows AFTER all keyword rows.

### Sitelink rows (campaign-level — applied to all ad groups):
```csv
Campaign,Action,Sitelink Text,Description Line 1,Description Line 2,Final URL
[Campaign Name],Add,[SL1 Title],[SL1 D1],[SL1 D2],[SL1 URL]
[Campaign Name],Add,[SL2 Title],[SL2 D1],[SL2 D2],[SL2 URL]
[Campaign Name],Add,[SL3 Title],[SL3 D1],[SL3 D2],[SL3 URL]
[Campaign Name],Add,[SL4 Title],[SL4 D1],[SL4 D2],[SL4 URL]
[Campaign Name],Add,[SL5 Title],[SL5 D1],[SL5 D2],[SL5 URL]
[Campaign Name],Add,[SL6 Title],[SL6 D1],[SL6 D2],[SL6 URL]
```

### Callout rows (campaign-level):
```csv
Campaign,Action,Callout Text
[Campaign Name],Add,[C1]
[Campaign Name],Add,[C2]
[Campaign Name],Add,[C3]
[Campaign Name],Add,[C4]
[Campaign Name],Add,[C5]
[Campaign Name],Add,[C6]
```

### Structured Snippet rows (campaign-level):
```csv
Campaign,Action,Structured Snippet Header,Structured Snippet Values
[Campaign Name],Add,[Header Type],"[V1]; [V2]; [V3]; [V4]; [V5]; [V6]"
```

---

## Output 5: Extensions in Microsoft Ads Bulk CSV

Extensions appended after keyword rows in Bing CSV.

### Sitelink Extension rows:
```csv
Type,Status,Campaign,Sitelink Extension Text,Description 1,Description 2,Final URL
Sitelink Extension,Active,[Campaign],[SL1 Title],[SL1 D1],[SL1 D2],[SL1 URL]
Sitelink Extension,Active,[Campaign],[SL2 Title],[SL2 D1],[SL2 D2],[SL2 URL]
Sitelink Extension,Active,[Campaign],[SL3 Title],[SL3 D1],[SL3 D2],[SL3 URL]
Sitelink Extension,Active,[Campaign],[SL4 Title],[SL4 D1],[SL4 D2],[SL4 URL]
Sitelink Extension,Active,[Campaign],[SL5 Title],[SL5 D1],[SL5 D2],[SL5 URL]
Sitelink Extension,Active,[Campaign],[SL6 Title],[SL6 D1],[SL6 D2],[SL6 URL]
```

### Callout Extension rows:
```csv
Type,Status,Campaign,Callout Text
Callout Extension,Active,[Campaign],[C1]
Callout Extension,Active,[Campaign],[C2]
Callout Extension,Active,[Campaign],[C3]
Callout Extension,Active,[Campaign],[C4]
Callout Extension,Active,[Campaign],[C5]
Callout Extension,Active,[Campaign],[C6]
```

### Structured Snippet Extension rows:
```csv
Type,Status,Campaign,Structured Snippet Header,Structured Snippet Values
Structured Snippet Extension,Active,[Campaign],[Header],"[V1]; [V2]; [V3]; [V4]; [V5]; [V6]"
```
