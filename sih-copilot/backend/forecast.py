import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "forecast.json"
)


def _load_forecast_data() -> dict[str, Any]:
    """
    Load prediction data from the mock JSON data source.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_forecasts() -> list[dict[str, Any]]:
    """
    Return all currently available predictions.
    """

    data = _load_forecast_data()

    return data["predictions"]


def get_footfall_forecasts() -> list[dict[str, Any]]:
    """
    Return predicted future footfall.
    """

    forecasts = get_forecasts()

    return [
        forecast
        for forecast in forecasts
        if forecast["metric"] == "footfall"
    ]


def get_forecast_by_id(
    forecast_id: str
) -> dict[str, Any] | None:
    """
    Return a specific forecast by ID.
    """

    forecasts = get_forecasts()

    for forecast in forecasts:
        if forecast["forecast_id"] == forecast_id:
            return forecast

    return None