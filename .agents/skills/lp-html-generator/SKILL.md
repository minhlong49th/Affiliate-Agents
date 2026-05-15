---
name: lp-html-generator
description: Worker 3 (final step) in the LP builder pipeline. For coupon LPs, renders HTML via the Jinja2 template script using run_command. For non-coupon LPs, generates HTML from scratch using the design system. Read this skill when executing the HTML generation phase. Do NOT use directly — invoked by lp-affiliate-pipeline.
---

# LP HTML Generator — Antigravity Worker 3

You are a precision HTML renderer for affiliate landing pages.
Your job: produce WordPress-ready HTML from the content blueprint.

---

## ROUTING: Check LP Type First

Use `view_file` to read `./output/[brand_slug]/.content_blueprint.json` and check `lp_type`.

**IF `lp_type` == `"coupon"`** → follow COUPON LP PATH (Jinja2 script via run_command).
**IF `lp_type` != `"coupon"`** → follow NON-COUPON LP PATH (prompt-based generation).

---

## COUPON LP PATH (Script-Based)

### Step 1 — Read & Validate Input

Use `view_file` to read `./output/[brand_slug]/.content_blueprint.json`.
Extract `brand_slug` and `lp_type`.

### Step 1.5 — Schema Validation (MANDATORY before running script)

Verify these required keys exist and are non-empty:

| Key | Type | Check |
|---|---|---|
| `meta_title` | string | non-empty |
| `brand_name` | string | non-empty |
| `affiliate_url` | string | non-empty |
| `slug` | string | non-empty |
| `colors.brand` | string | hex like `#XXXXXX` |
| `hero.eyebrow` | string | non-empty |
| `hero.headline_accent` | string | non-empty |
| `hero.sub` | string | non-empty |
| `coupon.code` | string | non-empty (e.g. `"AUTO-APPLIED"`) |
| `coupon.usage_seed` | number | integer |
| `intro.paragraphs` | array | at least 1 item |
| `verdict.score` | string | like `"8.5"` |
| `verdict.pros` | array | at least 1 item |
| `verdict.cons` | array | at least 1 item |
| `deals` | array | at least 1 item |
| `faq` | array | at least 1 item with `.q` and `.a` |
| `final_cta.headline` | string | non-empty |
| `final_cta.btn_label` | string | non-empty |
| `sticky_footer.text` | string | non-empty |

If ANY required field is missing or empty: report exactly which fields are absent. STOP. Do NOT run the script.

### Step 2 — Run the Render Script

Use `run_command`:
```powershell
python scripts/generate_lp_coupon_page.py `
  --data "./output/<brand_slug>/.content_blueprint.json" `
  --slug "<brand_slug>" `
  --out "./output/<brand_slug>/"
```

This produces `./output/<brand_slug>/<brand_slug>.html`.

### Step 3 — Rename to Final Output

Use `run_command`:
```powershell
Rename-Item -Path "./output/<brand_slug>/<brand_slug>.html" `
            -NewName "<brand_slug>-coupon-lp.html"
```

### Step 4 — Verify Output

Run these checks via `run_command`:

```powershell
# Check file exists and has content
$f = "./output/<brand_slug>/<brand_slug>-coupon-lp.html"
if ((Test-Path $f) -and (Get-Item $f).Length -gt 0) { "HAS_CONTENT" } else { "EMPTY_FILE" }

# Check for placeholder tokens
Select-String -Path $f -Pattern '\[[A-Z_]+\]' | Select-Object -First 5
if (-not $?) { "NO_PLACEHOLDERS" }

# Check for unrendered Jinja2 variables
Select-String -Path $f -Pattern '\{\{' | Select-Object -First 5
if (-not $?) { "NO_TEMPLATE_VARS" }

# Check for wrapper class
if (Select-String -Path $f -Pattern 'claude-lp-wrapper' -Quiet) { "WRAPPER_OK" }

# Check for coupon reveal JS
if (Select-String -Path $f -Pattern 'coupon-reveal-btn' -Quiet) { "JS_OK" }
```

If any check fails: log the failure and warn "Manual review recommended" — but still complete.

---

## NON-COUPON LP PATH (Prompt-Based)

For review, comparison, advertorial, and quiz LP.

### Inputs

Use `view_file` to read:
- `./output/[brand_slug]/.content_blueprint.json` — approved content
- `./knowledge/html_design_system_lite.md` — ALL CSS variables, components, and rules

### CRITICAL CSS ISOLATION (REQUIRED FOR WORDPRESS)

ALL HTML must be wrapped in:
```html
<div class="claude-lp-wrapper">
  ...
</div>
```

ALL CSS selectors must be prefixed with `.claude-lp-wrapper`:
```css
/* CORRECT */
.claude-lp-wrapper .hero-section { ... }
.claude-lp-wrapper h1 { ... }

/* WRONG — will break WordPress theme */
.hero-section { ... }
h1 { ... }
```

### HTML STRUCTURE (by lp_type)

#### Review LP order:
1. `<style>` block (all CSS inline, prefixed)
2. Hero section (H1 + subheadline + CTA button)
3. Coupon reveal box (code + copy button + GA4 event)
4. Brand overview
5. Benefits (outcome-focused)
6. Verdict box (pros + cons + recommendation)
7. FAQ
8. Final CTA
9. Footer disclosure

#### Comparison LP order:
1. Hero
2. Brand overview (lead with recommended brand)
3. Comparison table (3–5 rows, brand vs competitor)
4. Benefits of affiliate brand
5. FAQ
6. CTA + footer

#### Advertorial LP order:
1. Hook headline (no brand name above fold)
2. Story arc (problem → agitate → solution reveal)
3. Brand introduction (positioned as discovery)
4. Benefits
5. Social proof
6. CTA + footer

#### Quiz LP order:
1. Quiz intro + start button
2. Quiz phase 1–3 (questions with progress bar)
3. Result page (personalized recommendation)
4. CTA + footer

### REQUIRED JAVASCRIPT (inline `<script>` tag)

#### Coupon reveal mechanic:
```javascript
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.querySelector('.claude-lp-wrapper .reveal-btn');
  var codeBox = document.querySelector('.claude-lp-wrapper .coupon-code-box');
  if (btn && codeBox) {
    btn.addEventListener('click', function() {
      codeBox.style.display = 'block';
      btn.style.display = 'none';
      if (typeof gtag === 'function') {
        gtag('event', 'coupon_reveal', {
          'brand': '[brand_name]',
          'coupon_code': '[coupon_code]'
        });
      }
      var copyBtn = document.querySelector('.claude-lp-wrapper .copy-btn');
      if (copyBtn) {
        copyBtn.addEventListener('click', function() {
          navigator.clipboard.writeText('[coupon_code]').catch(function() {
            var el = document.createElement('textarea');
            el.value = '[coupon_code]';
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
          });
          copyBtn.textContent = 'Copied!';
        });
      }
    });
  }
});
```

#### Affiliate links — UTM parameters (apply to ALL outbound links):
```
[affiliate_url]?utm_source=organic&utm_medium=lp&utm_campaign=[brand-slug]-[lp-type]
```

### PLACEHOLDER CHECK (MANDATORY before saving)

Scan generated HTML for:
- Any `[` character in visible text
- Any `{{` template variable not replaced
- Any `null` rendered as literal text

If found: replace with appropriate fallback or remove section. Do NOT output a file with visible placeholder text.

### OUTPUT

Use `write_to_file` to save final HTML to:
`./output/[brand_slug]/[brand-slug]-[lp-type]-lp.html`

File must be self-contained:
- All CSS in `<style>` tag (no external stylesheets)
- All JS in `<script>` tag (no CDN dependencies)
- No external images (use CSS gradients/colors only)
- Mobile-responsive (system fonts only)
- No `<html>`, `<head>`, or `<body>` tags — WordPress-paste-ready block only

---

After saving HTML, return to orchestrator (`lp-affiliate-pipeline`) to proceed to Step 6 (Final Output Report).
