import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "inventory.json"
)


def _load_inventory_data() -> dict[str, Any]:
    """
    Load inventory data from the mock JSON data source.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_inventory() -> list[dict[str, Any]]:
    """
    Return the current inventory of all products.
    """

    data = _load_inventory_data()

    return data["products"]


def get_product_inventory(
    product_id: str
) -> dict[str, Any] | None:
    """
    Return inventory information for a specific product.
    """

    products = get_all_inventory()

    for product in products:
        if product["product_id"] == product_id:
            return product

    return None


def get_low_stock_items() -> list[dict[str, Any]]:
    """
    Return products whose stock is at or below
    their configured threshold.
    """

    products = get_all_inventory()

    return [
        product
        for product in products
        if product["stock"] <= product["threshold"]
    ]