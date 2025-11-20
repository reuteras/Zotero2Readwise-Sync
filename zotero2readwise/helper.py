import json
from pathlib import Path

from pyzotero.zotero import Zotero

from zotero2readwise import FAILED_ITEMS_DIR

ZOTERO_VERSION_FILE = FAILED_ITEMS_DIR.joinpath("zotero_version.json")


def read_library_version() -> int:
    """Read Zotero library version from a file in the home directory."""
    if not ZOTERO_VERSION_FILE.exists():
        return 0
    with open(ZOTERO_VERSION_FILE, "r") as f:
        return json.load(f)["version"]


def write_library_version(zotero_client: Zotero) -> None:
    """Read Zotero library version to a file in the home directory."""
    FAILED_ITEMS_DIR.mkdir(parents=True, exist_ok=True)
    with open(ZOTERO_VERSION_FILE, "w") as f:
        json.dump({"version": zotero_client.last_modified_version}, f)
