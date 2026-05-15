"""Check data quality flags from brand_data.json."""
import json
import sys

FLAG_MAP = {
    "AFFILIATE_LINK_UNVERIFIED": {
        "level": "STOP",
        "msg": "Affiliate link not confirmed live.",
    },
    "COMMISSION_BELOW_FLOOR": {
        "level": "WARN",
        "msg": "Commission < $8/sale. ROAS unlikely positive.",
    },
    "RATING_BELOW_THRESHOLD": {
        "level": "WARN",
        "msg": "Brand rating < 3.5 stars. Conversion challenges likely.",
    },
    "PPC_POLICY_UNKNOWN": {
        "level": "WARN",
        "msg": "Verify PPC policy before running Google Ads.",
    },
}


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/check_flags.py"
            " ./output/[brand_slug]/.brand_data.json"
        )
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = json.load(f)

    flags = data.get("data_quality", {}).get("flags", [])
    if not flags:
        print("No flags. Clean.")
        return

    print(f"Flags found ({len(flags)}):")
    for f in flags:
        info = FLAG_MAP.get(f, {"level": "WARN", "msg": "Unknown flag."})
        print(f"  [{info['level']}] {f} — {info['msg']}")


if __name__ == "__main__":
    main()
