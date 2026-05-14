# Reference 04 — Master Negative Keyword Library

## Structure: 3-Tier System

---

## TIER 1 — Account Level (apply to ALL campaigns, Broad Match)

These terms never convert for affiliate coupon/review campaigns.
Add to Shared Negative Keyword List in Google Ads / Shared Library in Microsoft Ads.

### No Purchase Intent
```
free
freebie
freebies
how to make
how to build
how to create
diy
do it yourself
homemade
wikipedia
definition
what is
meaning of
tutorial
guide for beginners
how to use
step by step
```

### Job Seekers
```
jobs
job
career
careers
hiring
hire
salary
salaries
wages
internship
internships
resume
cv
employment
employer
employers
recruiter
recruiting
recruitment
```

### Education / Research Only
```
certification
certifications
course
courses
training
learn
learning
school
university
college
student
students
academic
textbook
```

### Bad Traffic Sources
```
reddit
ebay
craigslist
amazon
etsy
walmart
facebook marketplace
temu
```

### Legal / Negative Sentiment
```
lawsuit
lawsuits
scam
scams
dangerous
side effects
recall
recalls
complaint
complaints
class action
bbb complaint
fraud
fraudulent
```

### Affiliate Industry (people researching affiliate, not buying)
```
affiliate program
affiliate commission
affiliate link
how affiliates work
become an affiliate
join affiliate
```

---

## TIER 2 — Campaign Level (per brand campaign, Phrase Match)

Generate dynamically based on brand research from Step 1.

### Template — fill in from brand data:
```
[competitor brand 1]
[competitor brand 2]
[unrelated product categories on LP if any]
wholesale
bulk
bulk order
bulk buy
reseller
distributor
for business
business pricing
commercial
enterprise
B2B
```

### For organic/garden niche specifically:
```
pesticide
herbicide
poison
chemical fertilizer
synthetic fertilizer
```

---

## TIER 3 — Ad Group Level (cross-contamination prevention, Exact Match)

**AG1 (Coupon Intent) negatives — block Product/Review terms from entering AG1:**
```
[review]
[reviews]
[vs]
[compare]
[comparison]
[alternative]
[alternatives]
[honest review]
[is worth it]
[legit]
[is it good]
```

**AG2 (Product/Review Intent) negatives — block Coupon terms from entering AG2:**
```
[coupon code]
[promo code]
[discount code]
[voucher code]
[savings code]
```
*(Only add these if both AG1 and AG2 exist in the same campaign)*

---

## Platform-Specific Negatives

### Microsoft Ads (Bing) — additional exclusions needed

**Site-level exclusions (add in campaign settings → placements):**
After launch, run Placement Report weekly and add low-quality domains to exclusion list.
Common Audience Network junk domains to pre-exclude:
```
games.lol
appnexus.com (low quality placements)
Any domain with: games, free, download, streaming
```

**Search Partners — disable immediately:**
In Microsoft Ads → Campaign Settings → Ad Distribution → uncheck "Search Partners"

---

## Negative Match Type Guide

| Term type | Match type to use | Why |
|---|---|---|
| Single word (free, jobs) | Broad Match | Blocks all queries containing this word |
| Multi-word intent phrase (how to make) | Phrase Match | Blocks exact phrase in any query |
| Very specific query (one-off bad term) | Exact Match | Surgical — doesn't over-block |
| Brand name of competitor | Phrase Match | Blocks [competitor] + any suffix |

---

## Negative Keyword CSV Output Format

For Google Ads Editor import:
```
Campaign, Ad Group, Keyword, Criterion Type
[Campaign Name], , [keyword], Negative Campaign
[Campaign Name], [Ad Group Name], [keyword], Negative Ad Group
```

For Microsoft Ads Bulk import:
```
Type, Campaign, Ad Group, Keyword, Match Type
Campaign Negative Keyword, [Campaign], , [keyword], Broad
Ad Group Negative Keyword, [Campaign], [Ad Group], [keyword], Exact
```

---

## Update Cadence (document in campaign brief)

- Weekly: Review Search Terms report → add new negatives found
- Monthly: Review and expand Tier 2 list with any new competitor names found
- Ongoing: Flag any keyword with CPC > $2.00 for negative consideration
