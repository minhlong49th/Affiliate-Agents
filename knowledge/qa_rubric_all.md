# QA Rubric ALL — Worker 4 Reference
# [DEPRECATED in Phase 1] Content moved inline to 04_qa_unified.md.
# This file is retained for reference but no longer injected to save tokens.

## RUBRIC A — FACTUAL ACCURACY

Score each claim in the content_blueprint against brand_data JSON.

| Check | PASS | FAIL |
|---|---|---|
| A1. Coupon code | Matches `coupon.code` or shows `[COUPON_CODE]` placeholder | Invented code not in brand_data |
| A2. Product prices | Match `price_usd` values or absent | Price stated but differs from brand_data |
| A3. Rating | Matches `social_proof.rating_stars` or absent | Different star rating used |
| A4. Review count | Matches `social_proof.review_count` or absent | Inflated/deflated count |
| A5. Commission | Not mentioned in copy (affiliate-internal only) | Commission % stated in public copy |
| A6. Affiliate URL | Consistent throughout | Mixed or broken affiliate links |
| A7. Brand facts | No invented founding year, team size, revenue | Invented statistics present |
| A8. Urgency Signals | Selected properly based on framework | Used banned fake urgency |

**Rubric A FAIL**: Any single A1, A2, or A7 failure = automatic FAIL. A3–A6 failures = WARN (flag but don't block).

---

## RUBRIC B — FRAMEWORK COMPLIANCE

### [TYPE: coupon]
| Check | PASS | FAIL |
|---|---|---|
| B1 | H1 contains primary keyword exactly | Paraphrased or missing |
| B2 | brand_overview agitates before revealing solution | Brand introduced positively first |
| B3 | Benefits written as outcomes ("you will...") | Feature-based benefits |
| B4 | Urgency signal is one of 5 approved types | Countdown timer / fake scarcity |
| B5 | No remaining `[` placeholders | Unfilled placeholder present |

### [TYPE: review]
| Check | PASS | FAIL |
|---|---|---|
| B1 | H1 contains primary keyword exactly | Paraphrased or missing |
| B2 | Verdict box present with clear PASS/CONDITIONAL/FAIL | No verdict box |
| B3 | Minimum 1 honest con (specific limitation) | No cons, or vague "price is high" |
| B4 | Benefits written as outcomes | Feature-based |
| B5 | FAQ uses skeptical/burned-user framing | FAQ reads like brand FAQ |

### [TYPE: comparison]
| Check | PASS | FAIL |
|---|---|---|
| B1 | H1 includes both brand names | Only one brand in H1 |
| B2 | Comparison table present with ≥5 criteria | Table absent or <5 criteria |
| B3 | Both brands scored fairly (not all wins to one side) | Obvious bias in table |
| B4 | Quick verdict states who wins AND for whom | Generic "Brand X is better" |

### [TYPE: advertorial]
| Check | PASS | FAIL |
|---|---|---|
| B1 | Brand name absent from first 60% of word count | Brand named before 60% mark |
| B2 | Hook headline has no brand name | Brand in headline |
| B3 | Story has identifiable protagonist with problem | Generic problem statement |
| B4 | False solutions section present | Jumps directly to brand |
| B5 | PAS structure: Problem → Agitate → Solution | Order violated |

### [TYPE: quiz]
| Check | PASS | FAIL |
|---|---|---|
| B1 | 3–4 questions with escalating commitment | Only 1 question or >6 |
| B2 | Result headline references quiz answers | Generic result |
| B3 | Result page: brand match tied to quiz profile | Generic brand pitch |

---

## SCORING DECISION

```
All Rubric A checks: PASS → A = PASS
Any A1/A2/A7 FAIL  → A = FAIL (must revise)

All Rubric B checks: PASS → B = PASS
Any 2+ B checks: FAIL → B = FAIL (must revise)
Exactly 1 B check FAIL → B = WARN (flag but can proceed)

Final result:
  A=PASS + B=PASS → PASS → proceed to Worker 3
  A=PASS + B=WARN → PASS WITH FLAGS → proceed with note
  A=FAIL OR B=FAIL → FAIL → send revision_instructions to Worker 2
```
