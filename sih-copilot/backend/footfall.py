import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "footfall.json"
)


def _load_footfall_data() -> dict[str, Any]:
    """
    Load footfall data from the mock JSON data source.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_current_footfall() -> dict[str, Any]:
    """
    Return the current store-wide footfall information.
    """

    data = _load_footfall_data()

    return {
        "store_id": data["store_id"],
        "last_updated": data["last_updated"],
        "current_footfall": data["current_footfall"]
    }


def get_section_footfall(
    section: str
) -> int | None:
    """
    Return the current footfall for a specific section.
    """

    data = _load_footfall_data()

    return data["sections"].get(section)


def get_historical_footfall() -> list[dict[str, Any]]:
    """
    Return historical footfall observations.
    """

    data = _load_footfall_data()

    return data["historical"]


def get_peak_footfall_period() -> dict[str, Any]:
    """
    Return the period with the highest observed footfall.
    """

    historical = get_historical_footfall()

    if not historical:
        return {}

    return max(
        historical,
        key=lambda record: record["footfall"]
    )