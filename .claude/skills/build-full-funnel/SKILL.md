---
name: build-full-funnel
description: >
  Run the full affiliate funnel: LP builder pipeline first, then PPC pipeline
  using the LP output as landing page URL. Use when asked to build everything,
  create a full funnel, or run both LP and PPC for a brand.
disable-model-invocation: true
argument-hint: <brand-url>
allowed-tools: Read, Write, Bash, Agent
---

Run the full affiliate funnel for $ARGUMENTS. LP pipeline runs first, then PPC pipeline chains automatically using the LP output URL.
Do NOT start Phase 2 until Phase 1 is fully complete.

## Pre-flight

- Run: `mkdir -p ./tmp ./output`
- Confirm $ARGUMENTS is not empty. If empty, stop and ask for a brand URL.

## Phase 1 — LP Builder Pipeline

Invoke the @lp-orchestrator agent with the full user input: $ARGUMENTS

The orchestrator will dispatch all LP workers sequentially and return:
- LP output file path: `./output/[brand-slug]/[brand-slug]-[lp-type]-lp.html`

Wait for LP BUILD COMPLETE signal.
Extract the output file path from the LP report.

## Phase 2 — PPC Builder Pipeline

After LP BUILD COMPLETE, immediately invoke the @ppc-orchestrator agent with:
- `landing_page_url`: the LP output file path from Phase 1 (or ask user for the live deployed URL)
- `platform`: both (default)
- `keyword_list`: reuse target keywords from the LP pipeline if available

The orchestrator will dispatch all PPC workers sequentially and return:
- Campaign brief markdown
- Google Ads CSV (if applicable)
- Bing Ads CSV (if applicable)

Wait for PPC CAMPAIGN BUILD COMPLETE signal.

## Done

Report:
- LP output: `./output/[brand-slug]/[brand-slug]-[lp-type]-lp.html`
- PPC brief: `./output/[brand-slug]/[brand-slug]-[platform]-campaign-brief.md`
- CSV files (if generated)
