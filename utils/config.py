import os


BASE_URL = os.getenv("QAFOX_BASE_URL", "https://www.qafox.com/").strip()
if not BASE_URL:
    raise ValueError("QAFOX_BASE_URL must not be empty.")
BASE_URL = f"{BASE_URL.rstrip('/')}/"

try:
    DEFAULT_TIMEOUT_MS = int(os.getenv("QAFOX_TIMEOUT_MS", "10000"))
except ValueError as error:
    raise ValueError("QAFOX_TIMEOUT_MS must be a positive integer.") from error

if DEFAULT_TIMEOUT_MS <= 0:
    raise ValueError("QAFOX_TIMEOUT_MS must be a positive integer.")
