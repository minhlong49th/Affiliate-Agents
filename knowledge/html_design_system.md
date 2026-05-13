# KNOWLEDGE: HTML Design System (FULL REFERENCE)
# [DEPRECATED in Phase 1] Use html_design_system_lite.md for injection.
# This file is retained for human reference (contains QA explanations) but is NO LONGER INJECTED.
# LP Builder Agent · ProductInsight Affiliate System
# Target: WordPress Custom HTML block compatible
# Last updated: April 2026

---

## 1. CORE CSS VARIABLES + ISOLATION WRAPPER

**All variables are scoped to `.claude-lp-wrapper`, NOT `:root`.**
This prevents CSS bleed into WordPress/GenerateBlocks host theme.

Merge this block with the `all: revert` reset (see Section 2) into a single rule — do NOT use two separate `.claude-lp-wrapper { }` blocks.

```css
.claude-lp-wrapper {
  /* === ISOLATION RESET (must be first) === */
  all: revert;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;

  /* === LAYOUT === */
  max-width: 720px;
  margin: 0 auto;
  padding: 0 20px;

  /* === Typography variables === */
  --font-base: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'Courier New', Courier, monospace;
  --size-base: 16px;
  --size-sm: 14px;
  --size-xs: 13px;
  --size-lg: 18px;
  --size-xl: 22px;
  --size-2xl: 28px;
  --size-3xl: 36px;
  --line-height: 1.75;
  --line-tight: 1.3;

  /* === Colors — neutral === */
  --color-text: #1a1a1a;
  --color-text-muted: #5a5a5a;
  --color-text-faint: #888;
  --color-bg: #ffffff;
  --color-bg-soft: #f7f7f5;
  --color-bg-card: #ffffff;
  --color-border: #e0deda;
  --color-border-strong: #c8c4be;

  /* === Colors — brand action (CTA) === */
  --color-cta-bg: #2d6a4f;        /* dark green — trust + organic niche */
  --color-cta-hover: #1b4332;
  --color-cta-text: #ffffff;
  --color-cta-secondary-bg: #f0faf5;
  --color-cta-secondary-border: #2d6a4f;
  --color-cta-secondary-text: #2d6a4f;

  /* === Colors — semantic === */
  --color-success: #2d6a4f;
  --color-warning: #92400e;
  --color-warning-bg: #fffbeb;
  --color-info: #1e3a5f;
  --color-info-bg: #eff6ff;

  /* === Colors — coupon reveal box === */
  --color-coupon-bg: #f0faf5;
  --color-coupon-border: #2d6a4f;
  --color-coupon-code: #1b4332;

  /* === Colors — verdict box === */
  --color-verdict-bg: #f7f7f5;
  --color-verdict-border: #e0deda;
  --color-verdict-highlight: #2d6a4f;

  /* === Layout tokens === */
  --max-width: 720px;
  --padding-x: 20px;
  --padding-section: 40px 20px;
  --border-radius: 8px;
  --border-radius-lg: 12px;
  --border-radius-pill: 999px;

  /* === Shadows === */
  --shadow-card: 0 1px 3px rgba(0,0,0,0.08);

  /* === Base styles (applied via wrapper) === */
  font-family: var(--font-base);
  font-size: var(--size-base);
  line-height: var(--line-height);
  color: var(--color-text);
  background: var(--color-bg);
}
```

---

## 2. BASE RESET + GLOBAL STYLES

All element selectors are prefixed with `.claude-lp-wrapper`. The wrapper's own reset is in Section 1.

```css
.claude-lp-wrapper *, .claude-lp-wrapper *::before, .claude-lp-wrapper *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.claude-lp-wrapper img { max-width: 100%; height: auto; display: block; }

.claude-lp-wrapper a { color: var(--color-cta-text); }
.claude-lp-wrapper a:hover { opacity: 0.85; }

.claude-lp-wrapper p { margin-bottom: 1rem; }
.claude-lp-wrapper p:last-child { margin-bottom: 0; }

.claude-lp-wrapper h1,
.claude-lp-wrapper h2,
.claude-lp-wrapper h3 { line-height: var(--line-tight); font-weight: 700; }
.claude-lp-wrapper h1 { font-size: var(--size-3xl); margin-bottom: 1rem; }
.claude-lp-wrapper h2 { font-size: var(--size-xl); margin-bottom: 0.75rem; }
.claude-lp-wrapper h3 { font-size: var(--size-lg); margin-bottom: 0.5rem; }

@media (max-width: 480px) {
  .claude-lp-wrapper h1 { font-size: var(--size-2xl); }
  .claude-lp-wrapper h2 { font-size: var(--size-lg); }
}

.claude-lp-wrapper ul,
.claude-lp-wrapper ol { padding-left: 1.5rem; margin-bottom: 1rem; }
.claude-lp-wrapper li { margin-bottom: 0.4rem; }
```

> **Note:** `.lp-wrapper` inner div is no longer used — the `max-width` and centering is applied directly on `.claude-lp-wrapper`.

---

## 3. COMPONENT LIBRARY

> All selectors below are already prefixed with `.claude-lp-wrapper`. Copy as-is into `<style>`.

### 3.1 CTA Button — Primary

```css
.claude-lp-wrapper .btn-primary {
  display: inline-block;
  background: var(--color-cta-bg);
  color: var(--color-cta-text);
  font-size: var(--size-lg);
  font-weight: 700;
  padding: 16px 32px;
  border-radius: var(--border-radius-pill);
  text-decoration: none;
  text-align: center;
  min-height: 54px;
  cursor: pointer;
  border: none;
  transition: background 0.15s ease;
  width: 100%;
}
.claude-lp-wrapper .btn-primary:hover { background: var(--color-cta-hover); color: #fff; }

@media (min-width: 480px) {
  .claude-lp-wrapper .btn-primary { width: auto; min-width: 280px; }
}
```

### 3.2 CTA Button — Secondary

```css
.claude-lp-wrapper .btn-secondary {
  display: inline-block;
  background: var(--color-cta-secondary-bg);
  color: var(--color-cta-secondary-text);
  font-size: var(--size-base);
  font-weight: 600;
  padding: 12px 24px;
  border-radius: var(--border-radius-pill);
  text-decoration: none;
  border: 2px solid var(--color-cta-secondary-border);
  min-height: 48px;
  cursor: pointer;
  transition: all 0.15s ease;
}
.claude-lp-wrapper .btn-secondary:hover {
  background: var(--color-cta-bg);
  color: white;
}
```

### 3.3 Coupon Reveal Box

```css
.claude-lp-wrapper .coupon-box {
  background: var(--color-coupon-bg);
  border: 2px solid var(--color-coupon-border);
  border-radius: var(--border-radius-lg);
  padding: 32px 24px;
  text-align: center;
  margin: 32px 0;
}

.claude-lp-wrapper .coupon-code-display {
  font-family: var(--font-mono);
  font-size: 2.5rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--color-coupon-code);
  margin: 16px 0;
  padding: 12px;
  background: white;
  border: 2px dashed var(--color-coupon-border);
  border-radius: var(--border-radius);
  word-break: break-all;
}

.claude-lp-wrapper .coupon-verified-note {
  font-size: var(--size-xs);
  color: var(--color-text-muted);
  margin-top: 12px;
}

.claude-lp-wrapper .coupon-btn-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 20px;
}

@media (min-width: 480px) {
  .claude-lp-wrapper .coupon-btn-group { flex-direction: row; justify-content: center; }
}
```

### 3.4 Verdict Box (Review LP)

```css
.claude-lp-wrapper .verdict-box {
  background: var(--color-verdict-bg);
  border: 1px solid var(--color-verdict-border);
  border-left: 4px solid var(--color-verdict-highlight);
  border-radius: var(--border-radius-lg);
  padding: 24px;
  margin: 28px 0;
}

.claude-lp-wrapper .verdict-rating {
  font-size: var(--size-xl);
  font-weight: 700;
  color: var(--color-verdict-highlight);
  margin-bottom: 4px;
}

.claude-lp-wrapper .verdict-rating-source {
  font-size: var(--size-xs);
  color: var(--color-text-muted);
  margin-bottom: 16px;
}

.claude-lp-wrapper .verdict-summary { font-size: var(--size-lg); margin-bottom: 12px; }

.claude-lp-wrapper .verdict-row {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
  font-size: var(--size-sm);
}

.claude-lp-wrapper .verdict-label {
  font-weight: 700;
  min-width: 80px;
  color: var(--color-text-muted);
  text-transform: uppercase;
  font-size: var(--size-xs);
  letter-spacing: 0.05em;
  padding-top: 2px;
}
```

### 3.5 Comparison Table

```css
.claude-lp-wrapper .comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 24px 0;
  font-size: var(--size-sm);
  overflow-x: auto;
  display: block;
}

.claude-lp-wrapper .comparison-table th {
  background: var(--color-bg-soft);
  font-weight: 700;
  padding: 12px 16px;
  text-align: left;
  border-bottom: 2px solid var(--color-border-strong);
  white-space: nowrap;
}

.claude-lp-wrapper .comparison-table th.col-brand {
  background: var(--color-coupon-bg);
  color: var(--color-coupon-code);
}

.claude-lp-wrapper .comparison-table td {
  padding: 10px 16px;
  border-bottom: 1px solid var(--color-border);
  vertical-align: top;
}

.claude-lp-wrapper .comparison-table tr:last-child td { border-bottom: none; }
.claude-lp-wrapper .comparison-table tr:hover td { background: var(--color-bg-soft); }

.claude-lp-wrapper .winner-badge {
  display: inline-block;
  background: var(--color-success);
  color: white;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--border-radius-pill);
  margin-left: 6px;
  vertical-align: middle;
}
```

### 3.6 FAQ — Expandable Items

```css
.claude-lp-wrapper .faq-section { margin: 40px 0; }

.claude-lp-wrapper .faq-item {
  border-bottom: 1px solid var(--color-border);
  padding: 4px 0;
}

.claude-lp-wrapper .faq-item summary {
  font-weight: 600;
  font-size: var(--size-base);
  padding: 16px 0;
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}

.claude-lp-wrapper .faq-item summary::-webkit-details-marker { display: none; }

.claude-lp-wrapper .faq-item summary::after {
  content: '+';
  font-size: var(--size-xl);
  font-weight: 400;
  color: var(--color-text-muted);
  flex-shrink: 0;
  line-height: 1;
  margin-top: 2px;
}

.claude-lp-wrapper .faq-item[open] summary::after { content: '−'; }

.claude-lp-wrapper .faq-answer {
  padding: 0 0 20px;
  color: var(--color-text);
  font-size: var(--size-sm);
  line-height: var(--line-height);
}
```

### 3.7 Benefit List

```css
.claude-lp-wrapper .benefit-list {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.claude-lp-wrapper .benefit-list li {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 10px 0;
  border-bottom: 1px solid var(--color-border);
  font-size: var(--size-base);
}

.claude-lp-wrapper .benefit-list li:last-child { border-bottom: none; }

.claude-lp-wrapper .benefit-icon {
  width: 20px;
  height: 20px;
  background: var(--color-success);
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 12px;
  font-weight: 700;
}
```

### 3.8 News Bar (Advertorial LP)

```css
.claude-lp-wrapper .news-bar {
  background: var(--color-bg-soft);
  border-bottom: 1px solid var(--color-border);
  padding: 8px var(--padding-x);
  font-size: var(--size-xs);
  color: var(--color-text-muted);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.claude-lp-wrapper .news-bar .sponsored-label {
  background: var(--color-bg-soft);
  border: 1px solid var(--color-border-strong);
  color: var(--color-text-muted);
  padding: 2px 8px;
  font-size: 11px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### 3.9 Quiz Components

```css
.claude-lp-wrapper .quiz-wrapper { padding: var(--padding-section); }

.claude-lp-wrapper .progress-bar-container {
  background: var(--color-border);
  border-radius: var(--border-radius-pill);
  height: 6px;
  margin-bottom: 8px;
  overflow: hidden;
}

.claude-lp-wrapper .progress-bar-fill {
  background: var(--color-success);
  height: 100%;
  border-radius: var(--border-radius-pill);
  transition: width 0.4s ease;
  width: 0%;
}

.claude-lp-wrapper .progress-text {
  font-size: var(--size-xs);
  color: var(--color-text-muted);
  margin-bottom: 24px;
}

.claude-lp-wrapper .question-block { display: none; }
.claude-lp-wrapper .question-block.active { display: block; }

.claude-lp-wrapper .question-text {
  font-size: var(--size-lg);
  font-weight: 600;
  margin-bottom: 20px;
}

.claude-lp-wrapper .answer-options { display: flex; flex-direction: column; gap: 10px; }

.claude-lp-wrapper .answer-option {
  background: var(--color-bg-soft);
  border: 2px solid var(--color-border);
  border-radius: var(--border-radius);
  padding: 14px 18px;
  cursor: pointer;
  font-size: var(--size-base);
  text-align: left;
  transition: all 0.15s ease;
  width: 100%;
}

.claude-lp-wrapper .answer-option:hover {
  border-color: var(--color-success);
  background: var(--color-coupon-bg);
}

.claude-lp-wrapper .result-block { display: none; }
.claude-lp-wrapper .result-block.active { display: block; }
```

### 3.10 Section Divider & Spacing

```css
.claude-lp-wrapper .section { padding: var(--padding-section); }
.claude-lp-wrapper .section + .section { padding-top: 0; }

.claude-lp-wrapper .section-divider {
  height: 1px;
  background: var(--color-border);
  margin: 32px 0;
}

.claude-lp-wrapper .card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-card);
  margin: 24px 0;
}

.claude-lp-wrapper .text-center { text-align: center; }
.claude-lp-wrapper .text-muted { color: var(--color-text-muted); font-size: var(--size-sm); }
.claude-lp-wrapper .text-small { font-size: var(--size-sm); }
.claude-lp-wrapper .text-xs { font-size: var(--size-xs); }
.claude-lp-wrapper .font-mono { font-family: var(--font-mono); }
```

### 3.11 P.S. Line

```css
.claude-lp-wrapper .ps-line {
  background: var(--color-bg-soft);
  border-left: 3px solid var(--color-border-strong);
  padding: 16px 20px;
  margin: 32px 0;
  font-size: var(--size-sm);
  color: var(--color-text);
  border-radius: 0 var(--border-radius) var(--border-radius) 0;
}
```

### 3.12 Footer / Disclosure

```css
.claude-lp-wrapper .lp-footer {
  background: var(--color-bg-soft);
  border-top: 1px solid var(--color-border);
  padding: 24px var(--padding-x);
  margin-top: 48px;
}

.claude-lp-wrapper .disclosure-text {
  font-size: var(--size-xs);
  color: var(--color-text-faint);
  line-height: 1.6;
  max-width: var(--max-width);
  margin: 0 auto;
}
```

---

## 4. PAGE SECTION TEMPLATES

> All content is inside `<div class="claude-lp-wrapper">` — no inner `.lp-wrapper` div needed.

### Header section
```html
<header class="section" style="padding-top: 48px;">
  <h1>[h1_content]</h1>
  <p class="text-muted">[subtitle or keyword phrase]</p>
</header>
```

### CTA section (centered)
```html
<div style="text-align:center; padding: 32px 20px;">
  <a href="[AFFILIATE_URL]?utm_source=organic&utm_medium=lp&utm_campaign=[brand-slug]"
     class="btn-primary">
    [CTA button text] →
  </a>
  <p class="text-xs text-muted" style="margin-top:12px;">
    [Coupon note or risk removal line]
  </p>
</div>
```

---

## 5. QA RULES FOR HTML OUTPUT

### Must-pass before delivery
```
CSS ISOLATION (check first):
□ Outermost element in <body> is <div class="claude-lp-wrapper">
□ .claude-lp-wrapper { } has `all: revert` as first property
□ CSS variables defined in .claude-lp-wrapper { } — NOT in :root { }
□ All CSS selectors prefixed: `.claude-lp-wrapper h1`, `.claude-lp-wrapper .btn-primary`, etc.
□ @media blocks: inner selectors also prefixed with .claude-lp-wrapper
□ No bare element or class selectors in <style> that could leak to host theme

CONTENT:
□ One <h1> only — no duplicate h1 tags
□ All <a> tags have non-empty, non-"#" href values
□ All affiliate links include UTM parameters
□ Coupon reveal button functions (test onclick handler)
□ Mobile viewport meta tag present in <head>
□ FTC disclosure in <footer>
□ No inline style uses position:fixed (breaks WordPress embedding)
□ No external CSS framework links (no Bootstrap, Tailwind CDN)
□ No external Google Fonts links (use system-ui instead)
□ Script tags placed before closing </body> tag
□ No remaining "[" placeholder characters
□ All section ids are unique on the page
□ <details>/<summary> FAQ items properly nested
□ Coupon code in monospace font (font-family: var(--font-mono))
□ CTA buttons minimum 48px height (min-height: 54px in CSS)
```

### WordPress Custom HTML compatibility rules
```
□ No <html>, <head>, or <body> tags in the pasted block
   (WordPress already provides these — paste only inner content)
   → Exception: if delivering as a standalone .html file,
     include full document structure
□ Inline <style> tags are permitted in WordPress Custom HTML
□ Inline <script> tags are permitted in WordPress Custom HTML
□ No relative file paths (no src="./image.jpg")
□ External images: use absolute URLs only, or omit images entirely
□ IDs must not conflict with WordPress default element IDs
   → Prefix all custom IDs with "lp-" to avoid conflicts
   → e.g., id="lp-coupon-box", id="lp-faq", id="lp-verdict"
□ Class names are isolated via .claude-lp-wrapper prefix — no conflicts expected
```

### Performance rules
```
□ No image elements unless brand provides an absolute URL
□ CSS kept in single <style> block — no multiple style tags
□ JS kept in single <script> block — no multiple script tags
□ Total file size target: under 50KB for text-only LP
□ No third-party analytics scripts (GA4 script already in WordPress theme)
   → Only fire gtag() events — assume gtag is already loaded
```

---

## 6. COLOR CUSTOMIZATION BY NICHE

Override variables inside `.claude-lp-wrapper { }` to match niche. Default above = organic/garden (green).
Add overrides after the main `.claude-lp-wrapper { }` block, or append them directly to it.
Override `--color-cta-bg`, `--color-cta-hover`, `--color-coupon-*`, `--color-verdict-highlight`, and `--color-success`.

---

## 7. PLACEHOLDER REFERENCE

All placeholders use square brackets. Search `[` before outputting to find unresolved ones.

| Placeholder | Description | Required |
|---|---|---|
| `[brand_name]` | Brand display name | Yes |
| `[brand-slug]` | Lowercase hyphenated brand | Yes |
| `[COUPON_CODE]` | Actual code or keep as placeholder | Yes (or note) |
| `[AFFILIATE_URL]` | Full redirect URL e.g. /go/buildasoil | Yes |
| `[lp-type]` | coupon / review / comparison / advertorial / quiz | Yes |
| `[h1_content]` | H1 headline text | Yes |
| `[meta.title]` | Browser tab title | Yes |
| `[current_date]` | ISO date of file generation | Yes |
| `[PERCENT_OFF]` | Discount percentage | If coupon available |
| `[THRESHOLD]` | Free shipping threshold | If known |
| `[RATING]` | Star rating from source | If known |
| `[RATING_SOURCE]` | Trustpilot / Google / Amazon | If rating present |
| `[COMPETITOR_NAME]` | Competitor brand name | Comparison LP only |