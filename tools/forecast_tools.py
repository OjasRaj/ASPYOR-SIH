from typing import Any

from backend.forecast import (
    get_forecasts,
    get_footfall_forecasts,
    get_forecast_by_id,
)


def tool_get_forecasts() -> dict[str, Any]:
    """
    Get all currently available predictions.
    """

    data = get_forecasts()

    return {
        "status": "success",
        "source": "forecast",
        "data": data
    }


def tool_get_footfall_forecasts() -> dict[str, Any]:
    """
    Get predicted future footfall.
    """

    data = get_footfall_forecasts()

    return {
        "status": "success",
        "source": "forecast",
        "data": data
    }


def tool_get_forecast(
    forecast_id: str
) -> dict[str, Any]:
    """
    Get a specific forecast by ID.
    """

    forecast = get_forecast_by_id(forecast_id)

    if forecast is None:
        return {
            "status": "not_found",
            "source": "forecast",
            "message": f"No forecast found with ID {forecast_id}."
        }

    return {
        "status": "success",
        "source": "forecast",
        "data": forecast
    }