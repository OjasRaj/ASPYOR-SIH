from tools.inventory_tools import (
    tool_get_inventory,
    tool_get_product_inventory,
    tool_get_low_stock_items,
)

from tools.footfall_tools import (
    tool_get_current_footfall,
    tool_get_section_footfall,
    tool_get_historical_footfall,
    tool_get_peak_footfall,
)

from tools.queue_tools import (
    tool_get_queue_status,
    tool_get_active_counters,
    tool_get_total_queue_length,
    tool_get_longest_queue,
)

from tools.sales_tools import (
    tool_get_sales_summary,
    tool_get_product_sales,
    tool_get_top_selling_products,
)

from tools.forecast_tools import (
    tool_get_forecasts,
    tool_get_footfall_forecasts,
    tool_get_forecast,
)


TOOL_REGISTRY = {
    "get_inventory": tool_get_inventory,
    "get_product_inventory": tool_get_product_inventory,
    "get_low_stock_items": tool_get_low_stock_items,

    "get_current_footfall": tool_get_current_footfall,
    "get_section_footfall": tool_get_section_footfall,
    "get_historical_footfall": tool_get_historical_footfall,
    "get_peak_footfall": tool_get_peak_footfall,

    "get_queue_status": tool_get_queue_status,
    "get_active_counters": tool_get_active_counters,
    "get_total_queue_length": tool_get_total_queue_length,
    "get_longest_queue": tool_get_longest_queue,

    "get_sales_summary": tool_get_sales_summary,
    "get_product_sales": tool_get_product_sales,
    "get_top_selling_products": tool_get_top_selling_products,

    "get_forecasts": tool_get_forecasts,
    "get_footfall_forecasts": tool_get_footfall_forecasts,
    "get_forecast": tool_get_forecast,
}