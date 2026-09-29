# ============================================================
# PDF Fusion & Security Manager
# File: config.py
# Purpose: Central configuration for the application
# ============================================================

APP_TITLE = "PDF Fusion & Security Manager"

# Default output file
DEFAULT_OUTPUT_FILE = "protected_merged.pdf"

# History file
HISTORY_FILE = "history.json"

# Maximum number of PDFs that can be selected
MAX_PDF_FILES = 20

# Application window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Supported file type
PDF_EXTENSION = ".pdf"

# Password settings
MIN_PASSWORD_LENGTH = 4

# Application information
APP_VERSION = "1.0.0"
APP_AUTHOR = "Student Project"

# Messages
MSG_NO_FILES = "Please select at least one PDF file."
MSG_INVALID_PDF = "The selected file is not a valid PDF."
MSG_PASSWORD_REQUIRED = "Please enter a password."
MSG_PASSWORD_MISMATCH = "Passwords do not match."
MSG_SUCCESS = "PDF created successfully."