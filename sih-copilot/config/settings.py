import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")


# --------------------------------------------------
# Application Configuration
# --------------------------------------------------

APP_ENV = os.getenv("APP_ENV", "development")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "5000"))


# --------------------------------------------------
# LLM Configuration
# --------------------------------------------------

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv("GROQ_MODEL")


# --------------------------------------------------
# Alert Configuration
# --------------------------------------------------

INVENTORY_THRESHOLD = int(
    os.getenv("INVENTORY_THRESHOLD", "10")
)

PREDICTION_ALERT_LEAD_MINUTES = int(
    os.getenv("PREDICTION_ALERT_LEAD_MINUTES", "60")
)


# --------------------------------------------------
# Data Directories
# --------------------------------------------------

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

LOG_DIR = BASE_DIR / "logs"