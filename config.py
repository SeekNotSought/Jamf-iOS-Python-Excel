# config.py
import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

JAMF_URL = os.getenv("JAMF_URL")
JAMF_USERNAME = os.getenv("JAMF_USERNAME")
JAMF_PASSWORD = os.getenv("JAMF_PASSWORD")

def validate_config():
    """Ensure all required environment variables are present."""
    missing = [k for k in ["JAMF_URL", "JAMF_USERNAME", "JAMF_PASSWORD"] if os.getenv(k) is None]
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")