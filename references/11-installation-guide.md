# Reference 11 — Installation & Usage Guide
## ppc-ad-copy-builder.skill
### Works with: Google Antigravity · Claude Code · Cursor · VS Code · Manual (Claude.ai)

---

## OVERVIEW

This skill file (`ppc-ad-copy-builder.skill`) is a self-contained AI agent package built on the
open SKILL.md standard (agentskills.io). It works in any environment that supports SKILL.md:
Antigravity (preferred), Claude Code, Cursor, VS Code with Claude extension.

**What it does in one sentence:** Give it a landing page URL → it reads the page, builds a
complete Google Ads + Bing Ads campaign with RSA copy, keywords, negatives, sitelinks, callout
extensions, structured snippets, and exports import-ready CSV files.

---

## METHOD 1 — GOOGLE ANTIGRAVITY (Preferred for ProductInsight)

Antigravity is the recommended runner because it supports multi-step agentic workflows natively.

### Step 1: Install the skill file
```
1. Open Antigravity
2. Go to: Settings → Skills → Install Skill
3. Click "Choose File" → select ppc-ad-copy-builder.skill
4. Skill appears in skill list as "ppc-ad-copy-builder"
5. Click "Activate" — toggle should turn green
```

### Step 2: Configure model settings (recommended)
```
In Antigravity → Settings → Model:
- Primary model: Claude Sonnet (for main generation)
- Web fetch: Enabled (required for LP analysis in Step 1)
- Max steps: 15 (skill uses up to 9 steps including extensions)
- Output directory: /templates/ (or your preferred output folder)
```

### Step 3: Run the skill — basic usage
```
Trigger phrase (type in Antigravity chat):
"Build PPC campaign for [URL] on [platform]"

Examples:
"Build PPC campaign for https://buildasoil.com on both"
"Create Google Ads campaign for https://seedshere.com — coupon intent only"
"Build Bing ads for https://myfarm.com — I'll provide keywords"
```

### Step 4: Provide optional inputs when prompted
```
The skill will ask if inputs are missing:
→ Keywords: paste list or say "auto-generate"
→ Ad group type: say "coupon", "review", "both", or "auto-detect"
→ Platform: "google", "bing", or "both"
```

### Step 5: Retrieve output files
```
Antigravity saves to your configured output directory:
- [brand]-campaign-brief.md    ← human-readable summary
- [brand]-google-ads-import.csv
- [brand]-bing-ads-import.csv
```

### Antigravity — Batch mode
```
"Build PPC campaigns for these brands:
1. https://buildasoil.com — google — coupon
2. https://seedsnow.com — both — review
3. https://foxfarm.com — bing — auto"

Skill runs brands sequentially, generates separate files per brand,
then outputs a batch summary report.
```

---

## METHOD 2 — CLAUDE CODE (Terminal)

Claude Code gives you full filesystem access and can write output files directly.

### Step 1: Install skill
```bash
# Navigate to your skills directory
cd ~/.claude/skills/

# Unzip the skill file
unzip ppc-ad-copy-builder.skill -d ppc-ad-copy-builder/

# Verify structure
ls ppc-ad-copy-builder/
# Should show: SKILL.md  references/  templates/
```

### Step 2: Start Claude Code with skill context
```bash
# From your project directory
claude --skill ~/.claude/skills/ppc-ad-copy-builder/SKILL.md

# Or set as default skill in .claude/config.json:
{
  "skills": ["~/.claude/skills/ppc-ad-copy-builder"]
}
```

### Step 3: Run via prompt
```
You: Build PPC campaign for https://buildasoil.com on both Google and Bing
Claude: [reads SKILL.md, fetches LP, runs 7-step pipeline, writes output files]
```

### Step 4: Output files
```bash
# Files written to current directory by default
ls *.csv *.md
# buildasoil-campaign-brief.md
# buildasoil-google-ads-import.csv
# buildasoil-bing-ads-import.csv
```

### Claude Code — useful flags
```bash
# Set custom output directory
claude --skill ./ppc-ad-copy-builder/SKILL.md --output-dir ./campaigns/

# Run in non-interactive mode (for scripting)
claude --skill ./ppc-ad-copy-builder/SKILL.md --message "Build campaign for https://example.com on google"
```

---

## METHOD 3 — CURSOR / VS CODE

### Step 1: Install skill
```
1. Unzip ppc-ad-copy-builder.skill to: .cursor/skills/ppc-ad-copy-builder/
   (or .vscode/skills/ for VS Code)
2. In Cursor: Cmd+Shift+P → "Claude: Load Skill" → select ppc-ad-copy-builder/SKILL.md
3. Skill is now active in your workspace
```

### Step 2: Use in Cursor Chat or Composer
```
Open Cursor Chat (Cmd+L) and type:
"Build PPC campaign for [URL]"

Cursor will read the skill and run the pipeline.
Output files appear in your project root.
```

---

## METHOD 4 — MANUAL (Claude.ai — current session approach)

No installation needed. Copy-paste the SKILL.md content to prime Claude.

### Step 1: Open Claude.ai and start new conversation

### Step 2: Paste SKILL.md as system context
```
Copy the entire content of ppc-ad-copy-builder/SKILL.md and paste it at the start
of your conversation with this prefix:

"Follow this skill specification exactly:

[paste SKILL.md content here]

---
Now run the skill with: [URL] on [platform]"
```

### Step 3: Provide reference files when needed
```
When Claude says "Read: references/05-rsa-copywriting.md", paste that file's content.
The skill is designed to work with just the main SKILL.md for light use cases.
For full output quality, paste the relevant reference file when Claude requests it.
```

### Step 4 — Faster manual method: Use pre-built prompts
```
Instead of pasting SKILL.md, use Prompt 01–11 from references/08-prompt-templates.md
as individual prompts in sequence. This is the most practical approach for Claude.ai.

Workflow:
1. Paste Prompt 01 (LP Analysis) → get brand research output
2. Paste Prompt 02 (Keyword Generation) → fill in [BRAND_DATA] from step 1
3. Paste Prompt 05 (RSA Generation) → fill in keyword + brand data
4. Paste Prompt 11 (Extensions) → fill in brand data
5. Paste Prompt 07 (CSV Export) → combine all outputs into CSV
```

---

## TRIGGER PHRASES (works across all methods)

The skill triggers on any of these phrases:

| Trigger | What it does |
|---|---|
| "Build PPC campaign for [URL]" | Full 7-step pipeline |
| "Create Google Ads for [URL]" | Google only, full pipeline |
| "Create Bing Ads for [URL]" | Bing only, full pipeline |
| "Write ad copy for [URL]" | Steps 1–6, no CSV |
| "Generate RSA headlines for [brand]" | Step 5 only |
| "Build sitelinks for [brand]" | Step 5.5 extensions only |
| "Generate keywords for [brand]" | Steps 1–4 only |
| "Check my ad copy for policy" | Step 6 QA only |
| "Analyze my campaign performance" | Kill/Scale mode |
| "Batch campaigns for [list of URLs]" | Batch mode |

---

## INPUT FORMAT REFERENCE

### Minimal input (auto-detect everything):
```
Build PPC campaign for https://buildasoil.com on both
```

### Full input (specify everything):
```
Build PPC campaign:
URL: https://buildasoil.com
Keywords: buildasoil coupon, buildasoil promo code, buildasoil review, buildasoil vs fox farm
Ad group type: coupon, review
Platform: both
```

### With existing keywords from GKP:
```
Build campaign for https://buildasoil.com
Platform: google
Keywords (from Google Keyword Planner, paste as-is):
buildasoil coupon — 1,000/mo
buildasoil promo code — 880/mo
buildasoil review — 590/mo
buildasoil potting soil — 320/mo
build a soil coupon — 260/mo
```
*(skill will parse volume data and incorporate into brief)*

---

## OUTPUT FILES GUIDE

### 1. `[brand]-campaign-brief.md`
Human-readable markdown — open in Notion, Obsidian, VS Code, or any markdown viewer.
Contains: full campaign structure, ad copy table with char counts, QA log, import instructions.

### 2. `[brand]-google-ads-import.csv`
Import via: Google Ads Editor → File → Import → From File
Contains: campaign rows, ad group rows, RSA ad rows, keyword rows, negative keyword rows,
sitelink extension rows, callout extension rows, structured snippet rows.

### 3. `[brand]-bing-ads-import.csv`
Import via: Microsoft Advertising Editor → File → Import → From File (or From Google Ads)
Contains: same structure as Google CSV, with Bing-specific column names.

**⚠️ Bing RSA note:** Microsoft Ads Editor handles RSA 15-headline format natively — after
importing campaign/keyword structure, enter RSA headlines manually in Editor's RSA creation
wizard by copying from the campaign brief.

---

## IMPORT WORKFLOW — STEP BY STEP

### Google Ads
```
1. Open Google Ads Editor (desktop app)
2. File → Import → From File → select [brand]-google-ads-import.csv
3. Review proposed changes in Editor
4. Click "Apply" for each entity type (Campaigns, Ad Groups, Ads, Keywords)
5. AFTER IMPORT — manual steps:
   a. Open RSA → Edit → Pin H1 to Position 1, H2 to Position 2
   b. Tools → Shared Library → Negative Keyword Lists → create list → apply to campaign
   c. Confirm all extensions are attached at campaign level
6. File → Post Changes (sends to Google for review)
```

### Microsoft Ads (Bing)
```
1. Open Microsoft Advertising Editor (desktop app)
2. File → Import → From File → select [brand]-bing-ads-import.csv
3. Review and apply all entities
4. For RSA: navigate to Ads → Responsive Search Ads → New RSA → paste headlines/descriptions
5. CRITICAL post-import steps:
   a. Campaign → Settings → Networks → UNCHECK "Search Partners"
   b. Campaign → Settings → Audience Network → add exclusion list of junk domains
   c. Set all keyword bids 20% lower than Google equivalents
6. Sync account → ads go to editorial review (typically 1 business day)
```

---

## TROUBLESHOOTING

| Problem | Cause | Fix |
|---|---|---|
| "LP fetch failed" | Cloudflare blocking, 403 error | Paste LP content manually into chat |
| "PPC HARD STOP" | Brand prohibits PPC | Verify with affiliate manager; do not launch |
| Headline over 30 chars | Auto-generation edge case | Manually trim; flag in QA log |
| CSV import error in Editor | Column mismatch | Open CSV in Excel → check column names vs Editor's template |
| RSA not showing in Bing | Bing RSA requires Editor entry | Use Editor RSA wizard for all 15 headlines |
| Extensions not showing | Not enough data / low QS | Wait 48–72h after launch; check extension approvals |
| "Manual Review Required" flag | 3 auto-fix attempts failed | Manually rewrite that specific asset |

---

## SKILL MAINTENANCE

### When to update the skill:
- Google Ads changes character limits (check quarterly)
- Microsoft Ads updates extension format
- New affiliate network added to your stack
- Platform adds new extension types (e.g., image extensions, price extensions)
- Joey Babineau or Crestani release updated strategy content

### How to update:
```
1. Open ppc-ad-copy-builder/references/[relevant-file].md
2. Update the relevant section
3. Re-run: python3 -c "import zipfile, os; ..." to repackage
4. Reinstall updated .skill file in Antigravity/Claude Code
```

### Version history:
```
v1.0 — April 2026: Initial release. Steps 1–7, Google + Bing CSV, PSBCU + 17-step.
v1.1 — April 2026: Added Step 5.5 (extensions), Prompt 11, References 10 + 11.
                   Added: 6 sitelinks, callouts, structured snippets per ad group.
                   Added: Installation guide for Antigravity, Claude Code, Cursor, manual.
                   Added: Extension QA checklist, platform differences section.
```
