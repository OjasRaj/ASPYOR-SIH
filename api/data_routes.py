from flask import Blueprint, jsonify

from backend.inventory import (
    get_all_inventory,
    get_product_inventory,
    get_low_stock_items,
)

from backend.footfall import (
    get_current_footfall,
    get_section_footfall,
    get_historical_footfall,
    get_peak_footfall_period,
)

from backend.queue import (
    get_queue_status,
    get_active_counters,
    get_total_queue_length,
    get_longest_queue,
)

from backend.sales import (
    get_sales_summary,
    get_product_sales,
    get_top_selling_products,
)

from backend.forecast import (
    get_forecasts,
    get_footfall_forecasts,
    get_forecast_by_id,
)


data_bp = Blueprint("data", __name__, url_prefix="/api")


# ==================================================
# INVENTORY
# ==================================================

@data_bp.get("/inventory")
def inventory():
    return jsonify({
        "status": "success",
        "source": "inventory",
        "data": get_all_inventory()
    })


@data_bp.get("/inventory/low-stock")
def low_stock_inventory():
    return jsonify({
        "status": "success",
        "source": "inventory",
        "count": len(get_low_stock_items()),
        "data": get_low_stock_items()
    })


@data_bp.get("/inventory/<product_id>")
def product_inventory(product_id: str):

    product = get_product_inventory(product_id)

    if product is None:
        return jsonify({
            "status": "not_found",
            "source": "inventory",
            "message": f"No product found with ID {product_id}."
        }), 404

    return jsonify({
        "status": "success",
        "source": "inventory",
        "data": product
    })


# ==================================================
# FOOTFALL
# ==================================================

@data_bp.get("/footfall/current")
def current_footfall():
    return jsonify({
        "status": "success",
        "source": "footfall",
        "data": get_current_footfall()
    })


@data_bp.get("/footfall/section/<section>")
def section_footfall(section: str):

    footfall = get_section_footfall(section)

    if footfall is None:
        return jsonify({
            "status": "not_found",
            "source": "footfall",
            "message": f"No data found for section {section}."
        }), 404

    return jsonify({
        "status": "success",
        "source": "footfall",
        "section": section,
        "footfall": footfall
    })


@data_bp.get("/footfall/history")
def historical_footfall():
    return jsonify({
        "status": "success",
        "source": "footfall",
        "data": get_historical_footfall()
    })


@data_bp.get("/footfall/peak")
def peak_footfall():
    return jsonify({
        "status": "success",
        "source": "footfall",
        "data": get_peak_footfall_period()
    })


# ==================================================
# QUEUE
# ==================================================

@data_bp.get("/queue/status")
def queue_status():
    return jsonify({
        "status": "success",
        "source": "queue",
        "data": get_queue_status()
    })


@data_bp.get("/queue/active")
def active_counters():
    data = get_active_counters()

    return jsonify({
        "status": "success",
        "source": "queue",
        "count": len(data),
        "data": data
    })


@data_bp.get("/queue/total")
def total_queue():
    return jsonify({
        "status": "success",
        "source": "queue",
        "total_waiting": get_total_queue_length()
    })


@data_bp.get("/queue/longest")
def longest_queue():
    data = get_longest_queue()

    if data is None:
        return jsonify({
            "status": "not_found",
            "source": "queue",
            "message": "No active checkout counters found."
        }), 404

    return jsonify({
        "status": "success",
        "source": "queue",
        "data": data
    })


# ==================================================
# SALES
# ==================================================

@data_bp.get("/sales/summary")
def sales_summary():
    return jsonify({
        "status": "success",
        "source": "sales",
        "data": get_sales_summary()
    })


@data_bp.get("/sales/product/<product_id>")
def product_sales(product_id: str):

    product = get_product_sales(product_id)

    if product is None:
        return jsonify({
            "status": "not_found",
            "source": "sales",
            "message": f"No sales data found for {product_id}."
        }), 404

    return jsonify({
        "status": "success",
        "source": "sales",
        "data": product
    })


@data_bp.get("/sales/top-products")
def top_selling_products():

    data = get_top_selling_products()

    return jsonify({
        "status": "success",
        "source": "sales",
        "count": len(data),
        "data": data
    })


# ==================================================
# FORECAST
# ==================================================

@data_bp.get("/forecast")
def forecasts():
    return jsonify({
        "status": "success",
        "source": "forecast",
        "data": get_forecasts()
    })


@data_bp.get("/forecast/footfall")
def footfall_forecasts():
    return jsonify({
        "status": "success",
        "source": "forecast",
        "data": get_footfall_forecasts()
    })


@data_bp.get("/forecast/<forecast_id>")
def forecast(forecast_id: str):

    data = get_forecast_by_id(forecast_id)

    if data is None:
        return jsonify({
            "status": "not_found",
            "source": "forecast",
            "message": f"No forecast found with ID {forecast_id}."
        }), 404

    return jsonify({
        "status": "success",
        "source": "forecast",
        "data": data
    })

@data_bp.get("/health")
def api_health():
    return jsonify({
        "status": "ok",
        "service": "retail-data-api"
    })