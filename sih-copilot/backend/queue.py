import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "queue.json"
)


def _load_queue_data() -> dict[str, Any]:
    """
    Load queue data from the mock JSON data source.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_queue_status() -> list[dict[str, Any]]:
    """
    Return the current status of all checkout counters.
    """

    data = _load_queue_data()

    return data["counters"]


def get_active_counters() -> list[dict[str, Any]]:
    """
    Return currently active checkout counters.
    """

    counters = get_queue_status()

    return [
        counter
        for counter in counters
        if counter["status"] == "active"
    ]


def get_total_queue_length() -> int:
    """
    Return the total number of customers currently waiting.
    """

    counters = get_queue_status()

    return sum(
        counter["queue_length"]
        for counter in counters
    )


def get_longest_queue() -> dict[str, Any] | None:
    """
    Return the counter with the longest active queue.
    """

    active_counters = get_active_counters()

    if not active_counters:
        return None

    return max(
        active_counters,
        key=lambda counter: counter["queue_length"]
    )