import json
import sys
from pathlib import Path

FAILED_ITEMS_DIR = Path.home().joinpath(".zotero2readwise")
FAILED_ITEMS_FILE = FAILED_ITEMS_DIR.joinpath("failed_zotero_items.json")

def report_failures():
    """
    Reads the failed items JSON file, reports a summary of the failures,
    and exits with a non-zero status code if failures are present.
    """
    if not FAILED_ITEMS_FILE.exists():
        print("No failed items found.")
        sys.exit(0)

    with open(FAILED_ITEMS_FILE, "r") as f:
        failed_items = json.load(f)

    if not failed_items:
        print("No failed items found.")
        sys.exit(0)

    print(f"Found {len(failed_items)} failed annotations:")
    for item in failed_items:
        data = item.get("item", {}).get("data", {})
        key = data.get("key")
        reason = item.get("reason", "Unknown reason")
        print(f"  - Item Key: {key}, Reason: {reason}")

    sys.exit(1)

if __name__ == "__main__":
    report_failures()
