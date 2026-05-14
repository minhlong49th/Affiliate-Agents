#!/usr/bin/env python3
"""
LP Generator — Batch HTML Landing Page Generator
ProductInsight / AffiliateOS

Usage:
  python generate.py                        # Generate ALL brands from brands.json
  python generate.py --slug courtside-tennis  # Generate one specific brand
  python generate.py --data data/brands.json  # Specify custom data file
  python generate.py --out output/           # Specify output directory
  python generate.py --list                  # List all slugs in data file
"""

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("❌ Jinja2 not installed. Run: pip install jinja2")
    sys.exit(1)


# ─── Config ────────────────────────────────────────────────────────────────────
BASE_DIR       = Path(__file__).parent.parent
TEMPLATE_DIR   = BASE_DIR / "templates"
TEMPLATE_FILE  = "lp_coupon_template.html"
DATA_FILE      = BASE_DIR / "docs" / "lp-generator" / "brands.json"
OUTPUT_DIR     = BASE_DIR / "output"


# ─── Jinja2 Setup ──────────────────────────────────────────────────────────────
def get_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,  # JSON data contains raw HTML tags — no escaping needed
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


# ─── Generator ─────────────────────────────────────────────────────────────────
def generate_page(brand_data: dict, env, output_dir: Path) -> Path:
    """Render one brand's landing page and write to disk."""
    slug = brand_data.get("slug")
    if not slug:
        raise ValueError(f"Brand entry missing 'slug': {brand_data.get('brand_name', '?')}")

    template = env.get_template(TEMPLATE_FILE)
    html = template.render(**brand_data)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{slug}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


def load_brands(data_file: Path) -> list[dict]:
    with open(data_file, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]  # Support single-brand JSON too
    return data


# ─── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="LP Generator — Batch HTML page generator")
    parser.add_argument("--slug",   help="Generate only this slug (skip others)")
    parser.add_argument("--data",   help="Path to JSON data file", default=str(DATA_FILE))
    parser.add_argument("--out",    help="Output directory", default=str(OUTPUT_DIR))
    parser.add_argument("--list",   help="List all slugs in data file", action="store_true")
    args = parser.parse_args()

    data_path  = Path(args.data)
    output_dir = Path(args.out)

    if not data_path.exists():
        print(f"❌ Data file not found: {data_path}")
        sys.exit(1)

    brands = load_brands(data_path)

    if args.list:
        print(f"\n📋 Brands in {data_path.name}:")
        for b in brands:
            print(f"  • {b.get('slug', '?')}  —  {b.get('brand_name', '?')}")
        print(f"\n  Total: {len(brands)} brands")
        return

    if args.slug:
        brands = [b for b in brands if b.get("slug") == args.slug]
        if not brands:
            print(f"❌ Slug '{args.slug}' not found in {data_path.name}")
            sys.exit(1)

    env = get_env()

    print(f"\n🚀 LP Generator — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   Data:   {data_path}")
    print(f"   Output: {output_dir}")
    print(f"   Pages:  {len(brands)}\n")

    ok, fail = 0, 0
    for brand in brands:
        slug = brand.get("slug", "unknown")
        try:
            out_path = generate_page(brand, env, output_dir)
            size_kb  = out_path.stat().st_size / 1024
            print(f"  ✅  {slug}.html  ({size_kb:.1f} KB)")
            ok += 1
        except Exception as e:
            print(f"  ❌  {slug}  →  {e}")
            fail += 1

    print(f"\n{'─'*40}")
    print(f"  Done: {ok} generated, {fail} failed")
    if ok:
        print(f"  📁 Output → {output_dir.resolve()}\n")


if __name__ == "__main__":
    main()
