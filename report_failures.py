import json
import sys
from pathlib import Path

FAILED_ITEMS_DIR = Path.home().joinpath(".zotero2readwise")
ZOTERO_FAILED_FILE = FAILED_ITEMS_DIR.joinpath("failed_zotero_items.json")
READWISE_FAILED_FILE = FAILED_ITEMS_DIR.joinpath("failed_readwise_items.json")

def report_failures():
    """
    Reads the failed items JSON files, reports a summary of the failures,
    and exits with a non-zero status code if failures are present.
    """
    zotero_failures = []
    if ZOTERO_FAILED_FILE.exists():
        with open(ZOTERO_FAILED_FILE, "r") as f:
            zotero_failures = json.load(f)

    readwise_failures = []
    if READWISE_FAILED_FILE.exists():
        with open(READWISE_FAILED_FILE, "r") as f:
            readwise_failures = json.load(f)

    if not zotero_failures and not readwise_failures:
        print("No failed items found.")
        sys.exit(0)

    if zotero_failures:
        print(f"Found {len(zotero_failures)} Zotero formatting failures:")
        for item in zotero_failures:
            data = item.get("item", {}).get("data", {})
            key = data.get("key")
            reason = item.get("reason", "Unknown reason")
            print(f"  - Item Key: {key}, Reason: {reason}")

    if readwise_failures:
        print(f"Found {len(readwise_failures)} Readwise conversion failures:")
        for item in readwise_failures:
            item_data = item.get("item", {})
            key = item_data.get("key")
            reason = item.get("reason", "Unknown reason")
            print(f"  - Item Key: {key}, Reason: {reason}")

    sys.exit(1)

if __name__ == "__main__":
    report_failures()
