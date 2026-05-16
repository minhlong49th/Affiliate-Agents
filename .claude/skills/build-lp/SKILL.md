---
name: build-lp
description: >
  Run the full LP builder pipeline for an affiliate brand.
  Use when asked to build a landing page, create an LP,
  or run the full pipeline for a brand. Supports coupon,
  review, comparison, advertorial, and quiz LP types.
disable-model-invocation: true
argument-hint: <brand-url>
allowed-tools: Read, Write, Bash, Agent
---

Run the full LP builder pipeline for $ARGUMENTS in this exact sequential order.
Do NOT start the next step until the previous step is fully complete.

## Pre-flight

- Run: `mkdir -p ./tmp ./output`
- Confirm $ARGUMENTS is not empty. If empty, stop and ask for a brand URL or brand name.
- Extract brand name from URL if provided (e.g. "buildasoil.com" → "buildasoil").

## Step 1 — Orchestrate

Invoke the @lp-orchestrator agent with the full user input: $ARGUMENTS

The orchestrator will:
1. Collect required inputs (brand_name, brand_url, affiliate_url, network)
2. Detect LP type
3. Dispatch all worker agents sequentially (researcher → content-builder → qa-checker → html-generator)
4. Return a final LP BUILD COMPLETE report

Wait for LP BUILD COMPLETE before finishing.

## Done

Report the output file path from the orchestrator's final report.
