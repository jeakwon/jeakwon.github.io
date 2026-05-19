#!/usr/bin/env python3
"""Fetch aggregate Google Scholar metrics (citations, h-index, i10-index)
and write _data/scholar_stats.yml.

Source of truth for the CV's Publication Summary section.

Safe-by-default: if the fetch fails (CAPTCHA, network, etc.), the existing
scholar_stats.yml is left untouched and the script exits 0 so CI can keep
publishing the CV with the last known good numbers.
"""

import os
import sys
from datetime import datetime

import yaml

try:
    from scholarly import scholarly
except ImportError:
    sys.exit("scholarly required: pip install scholarly")

SOCIALS_FILE = "_data/socials.yml"
OUTPUT_FILE = "_data/scholar_stats.yml"


def load_scholar_user_id() -> str:
    if not os.path.exists(SOCIALS_FILE):
        sys.exit(f"{SOCIALS_FILE} not found")
    with open(SOCIALS_FILE, "r") as f:
        config = yaml.safe_load(f)
    sid = config.get("scholar_userid")
    if not sid:
        sys.exit(f"'scholar_userid' missing in {SOCIALS_FILE}")
    return sid


def fetch_stats(scholar_id: str) -> dict | None:
    scholarly.set_timeout(20)
    scholarly.set_retries(2)
    try:
        author = scholarly.search_author_id(scholar_id)
        filled = scholarly.fill(author, sections=["indices"])
    except Exception as e:
        print(f"WARN: Scholar fetch failed: {e}", file=sys.stderr)
        return None
    return {
        "citations": int(filled.get("citedby", 0)),
        "h_index": int(filled.get("hindex", 0)),
        "i10_index": int(filled.get("i10index", 0)),
    }


def main() -> None:
    scholar_id = load_scholar_user_id()
    print(f"Fetching aggregate Scholar stats for {scholar_id}")
    stats = fetch_stats(scholar_id)
    if stats is None:
        print("Keeping existing scholar_stats.yml (no update written).")
        return
    data = {
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "scholar_userid": scholar_id,
        },
        "stats": stats,
    }
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"Wrote {OUTPUT_FILE}: {stats}")


if __name__ == "__main__":
    main()
