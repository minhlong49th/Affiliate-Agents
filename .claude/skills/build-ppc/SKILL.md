---
name: build-ppc
description: >
  Run the full PPC Ad Copy Builder pipeline for an affiliate campaign.
  Use when asked to build a campaign, write ad copy, create RSA ads,
  generate ad groups, or export Google/Bing Ads CSV files.
  Supports single brand, batch mode, and kill/scale analysis.
disable-model-invocation: true
argument-hint: <landing-page-url> [platform: google|bing|both]
allowed-tools: Read, Write, Bash, Agent
---

Run the full PPC builder pipeline for $ARGUMENTS in this exact sequential order.
Do NOT start the next step until the previous step is fully complete.

## Pre-flight

- Run: `mkdir -p ./output`
- Confirm $ARGUMENTS is not empty. If empty, stop and ask for a landing page URL.
- Detect platform from $ARGUMENTS (default: both).

## Step 1 — Orchestrate

Invoke the @ppc-orchestrator agent with the full user input: $ARGUMENTS

The orchestrator will:
1. Collect required inputs (landing_page_url, platform, keyword_list)
2. Detect mode (single / batch / kill_scale)
3. Dispatch all worker agents sequentially (lp-analyst → keyword-builder → ad-copy-writer → qa-compliance → output-exporter)
4. Return a PPC CAMPAIGN BUILD COMPLETE report with output file paths

Wait for PPC CAMPAIGN BUILD COMPLETE before finishing.

## Done

Report all output file paths from the orchestrator's final report.
