from typing import Any

from backend.queue import (
    get_queue_status,
    get_active_counters,
    get_total_queue_length,
    get_longest_queue,
)


def tool_get_queue_status() -> dict[str, Any]:
    """
    Get the current status of all checkout counters.
    """

    data = get_queue_status()

    return {
        "status": "success",
        "source": "queue",
        "data": data
    }


def tool_get_active_counters() -> dict[str, Any]:
    """
    Get all currently active checkout counters.
    """

    data = get_active_counters()

    return {
        "status": "success",
        "source": "queue",
        "count": len(data),
        "data": data
    }


def tool_get_total_queue_length() -> dict[str, Any]:
    """
    Get the total number of customers currently waiting.
    """

    total = get_total_queue_length()

    return {
        "status": "success",
        "source": "queue",
        "total_waiting": total
    }


def tool_get_longest_queue() -> dict[str, Any]:
    """
    Get the checkout counter with the longest queue.
    """

    data = get_longest_queue()

    if data is None:
        return {
            "status": "not_found",
            "source": "queue",
            "message": "No active checkout counters found."
        }

    return {
        "status": "success",
        "source": "queue",
        "data": data
    }