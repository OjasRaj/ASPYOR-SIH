from typing import Any

from backend.inventory import (
    get_all_inventory,
    get_product_inventory,
    get_low_stock_items,
)


def tool_get_inventory() -> dict[str, Any]:
    """
    Get the current inventory of all products.

    This tool is used when the Copilot needs general
    inventory information.
    """

    inventory = get_all_inventory()

    return {
        "status": "success",
        "source": "inventory",
        "data": inventory
    }


def tool_get_product_inventory(
    product_id: str
) -> dict[str, Any]:
    """
    Get inventory information for one product.
    """

    product = get_product_inventory(product_id)

    if product is None:
        return {
            "status": "not_found",
            "source": "inventory",
            "message": f"No product found with ID {product_id}."
        }

    return {
        "status": "success",
        "source": "inventory",
        "data": product
    }


def tool_get_low_stock_items() -> dict[str, Any]:
    """
    Get products whose stock is at or below
    their configured threshold.
    """

    low_stock = get_low_stock_items()

    return {
        "status": "success",
        "source": "inventory",
        "count": len(low_stock),
        "data": low_stock
    }