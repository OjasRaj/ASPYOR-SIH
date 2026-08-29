import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "sales.json"
)


def _load_sales_data() -> dict[str, Any]:
    """
    Load sales data from the mock JSON data source.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_sales_summary() -> dict[str, Any]:
    """
    Return the current sales summary.
    """

    data = _load_sales_data()

    return data["summary"]


def get_product_sales(
    product_id: str
) -> dict[str, Any] | None:
    """
    Return sales information for a specific product.
    """

    data = _load_sales_data()

    for product in data["products"]:
        if product["product_id"] == product_id:
            return product

    return None


def get_top_selling_products(
    limit: int = 5
) -> list[dict[str, Any]]:
    """
    Return the top-selling products based on units sold.
    """

    data = _load_sales_data()

    products = sorted(
        data["products"],
        key=lambda product: product["units_sold"],
        reverse=True
    )

    return products[:limit]