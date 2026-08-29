from typing import Any

from backend.footfall import (
    get_current_footfall,
    get_section_footfall,
    get_historical_footfall,
    get_peak_footfall_period,
)


def tool_get_current_footfall() -> dict[str, Any]:
    """
    Get the current store-wide footfall.
    """

    data = get_current_footfall()

    return {
        "status": "success",
        "source": "footfall",
        "data": data
    }


def tool_get_section_footfall(
    section: str
) -> dict[str, Any]:
    """
    Get the current footfall for a specific section.
    """

    footfall = get_section_footfall(section)

    if footfall is None:
        return {
            "status": "not_found",
            "source": "footfall",
            "message": f"No footfall data available for {section}."
        }

    return {
        "status": "success",
        "source": "footfall",
        "section": section,
        "footfall": footfall
    }


def tool_get_historical_footfall() -> dict[str, Any]:
    """
    Get historical footfall observations.
    """

    data = get_historical_footfall()

    return {
        "status": "success",
        "source": "footfall",
        "data": data
    }


def tool_get_peak_footfall() -> dict[str, Any]:
    """
    Get the period with the highest observed footfall.
    """

    data = get_peak_footfall_period()

    return {
        "status": "success",
        "source": "footfall",
        "data": data
    }