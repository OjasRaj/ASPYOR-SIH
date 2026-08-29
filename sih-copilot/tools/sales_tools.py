from typing import Any

from backend.sales import (
    get_sales_summary,
    get_product_sales,
    get_top_selling_products,
)


def tool_get_sales_summary() -> dict[str, Any]:
    """
    Get the current sales summary.
    """

    data = get_sales_summary()

    return {
        "status": "success",
        "source": "sales",
        "data": data
    }


def tool_get_product_sales(
    product_id: str
) -> dict[str, Any]:
    """
    Get sales information for a specific product.
    """

    product = get_product_sales(product_id)

    if product is None:
        return {
            "status": "not_found",
            "source": "sales",
            "message": f"No sales data found for {product_id}."
        }

    return {
        "status": "success",
        "source": "sales",
        "data": product
    }


def tool_get_top_selling_products(
    limit: int = 5
) -> dict[str, Any]:
    """
    Get the top-selling products.
    """

    data = get_top_selling_products(limit)

    return {
        "status": "success",
        "source": "sales",
        "count": len(data),
        "data": data
    }