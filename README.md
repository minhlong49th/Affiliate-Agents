# LP Builder Agent — Claude Code Setup

Multi-agent pipeline: 4 sub-agents chạy tuần tự để build affiliate landing pages.

---

## Cài đặt

### Option A — Project-level (recommended)

```bash
# Copy vào project của bạn
cp -r .claude/agents/ your-project/.claude/agents/
cp CLAUDE.md your-project/CLAUDE.md

# Copy knowledge files từ skill gốc
cp -r /path/to/lp-builder-agent/knowledge/ your-project/knowledge/

# Tạo output folder
mkdir your-project/output

# Mở Claude Code trong project
cd your-project
claude
```

### Option B — Global (dùng được ở mọi project)

```bash
# Copy agents vào global directory
cp .claude/agents/*.md ~/.claude/agents/

# Copy knowledge vào project khi cần
```

---

## Sử dụng

Trong Claude Code, chỉ cần gõ:

```
Build LP for BuildASoil — affiliate URL /go/buildasoil — GoAffPro — coupon
```

Hoặc:
```
Build review LP for SeedsNow.com
Affiliate URL: /go/seedsnow
Network: ShareASale
Keywords: seedsnow review, seedsnow seeds quality, is seedsnow legit
```

Claude Code sẽ tự động:
1. Kích hoạt `lp-orchestrator`
2. Orchestrator dispatch tuần tự 4 agents
3. Lưu HTML vào `./output/[brand_slug]/[brand]-[lp-type]-lp.html`

---

## File structure sau cài đặt

```
your-project/
├── CLAUDE.md                          ← Routing rules cho orchestrator
├── .claude/
│   └── agents/
│       ├── lp-orchestrator.md         ← Điều phối pipeline (Sonnet)
│       ├── lp-brand-researcher.md     ← Worker 1: Brand research (Haiku)
│       ├── lp-content-builder.md      ← Worker 2: Content blueprint (Sonnet)
│       ├── lp-qa-checker.md           ← Worker 4: QA scoring (Sonnet)
│       └── lp-html-generator.md       ← Worker 3: HTML render (Haiku)
├── knowledge/
│   ├── lp_framework_base.md
│   ├── lp_framework_coupon.md
│   ├── lp_framework_review.md
│   ├── lp_framework_comparison.md
│   ├── lp_framework_advertorial.md
│   ├── lp_framework_quiz.md
│   ├── copywriting_techniques.md
│   └── html_design_system_lite.md
└── output/
    └── [brand_slug]/
        ├── .pipeline_input.json
        ├── .brand_data.json
        ├── .content_blueprint.json
        ├── .qa_result.json
        └── [brand-slug]-[lp-type]-lp.html ← Generated files
```

---

## Model cost optimization

| Agent | Model | Token cost |
|---|---|---|
| lp-orchestrator | claude-sonnet-4-6 | Medium |
| lp-brand-researcher | claude-haiku-4-5-20251001 | Low |
| lp-content-builder | claude-sonnet-4-6 | High |
| lp-qa-checker | claude-sonnet-4-6 | Medium |
| lp-html-generator | claude-haiku-4-5-20251001 | Low |

Ước tính 1 run = ~15,000–25,000 tokens tổng (với QA pass lần đầu).

---

## Temp files

Pipeline tạo các file tạm trong `./output/[brand_slug]/`:
- `.pipeline_input.json` — parsed user input
- `.brand_data.json` — Worker 1 output
- `.content_blueprint.json` — Worker 2 output
- `.qa_result.json` — Worker 4 QA scores

Xóa sau khi HTML đã confirm: `rm -r ./output/[brand_slug]`
