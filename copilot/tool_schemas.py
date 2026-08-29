TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_inventory",
            "description": (
                "Get the current inventory of all products "
                "in the store."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_product_inventory",
            "description": (
                "Get current inventory information for a "
                "specific product."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "Product ID such as P001."
                    }
                },
                "required": ["product_id"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_low_stock_items",
            "description": (
                "Get all products whose current stock is "
                "at or below their configured threshold."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_current_footfall",
            "description": (
                "Get the current total store footfall."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_section_footfall",
            "description": (
                "Get the current footfall for a specific "
                "store section."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": (
                            "Store section such as Electronics, "
                            "Grocery, Clothing, or Home."
                        )
                    }
                },
                "required": ["section"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_historical_footfall",
            "description": (
                "Get historical store footfall observations."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_peak_footfall",
            "description": (
                "Get the period with the highest observed "
                "footfall."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_queue_status",
            "description": (
                "Get the current status of all checkout counters."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_active_counters",
            "description": (
                "Get all currently active checkout counters."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_total_queue_length",
            "description": (
                "Get the total number of customers currently "
                "waiting in checkout queues."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_longest_queue",
            "description": (
                "Get the checkout counter currently having "
                "the longest queue."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_sales_summary",
            "description": (
                "Get the current store sales summary including "
                "revenue, units sold, and transactions."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_product_sales",
            "description": (
                "Get sales information for a specific product."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "Product ID such as P001."
                    }
                },
                "required": ["product_id"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_top_selling_products",
            "description": (
                "Get the products with the highest number "
                "of units sold."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": (
                            "Maximum number of products to return."
                        ),
                        "default": 5
                    }
                },
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_forecasts",
            "description": (
                "Get all currently available predictions "
                "for the store."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_footfall_forecasts",
            "description": (
                "Get predicted future footfall for store sections."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_forecast",
            "description": (
                "Get a specific prediction using its forecast ID."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "forecast_id": {
                        "type": "string",
                        "description": "Forecast ID such as F001."
                    }
                },
                "required": ["forecast_id"]
            }
        }
    }
]