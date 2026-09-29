# ============================================================
# PDF Fusion & Security Manager
# File: history_manager.py
# Purpose: Store and manage PDF operation history
# ============================================================

import json
import os
from datetime import datetime

from config import HISTORY_FILE


class HistoryManager:
    """Manages application operation history."""

    def __init__(self, history_file=HISTORY_FILE):
        self.history_file = history_file

    # --------------------------------------------------------
    # LOAD HISTORY
    # --------------------------------------------------------

    def load_history(self):
        """Load existing history from the JSON file."""

        if not os.path.exists(self.history_file):
            return []

        try:
            with open(
                self.history_file,
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            if isinstance(data, list):
                return data

            return []

        except (json.JSONDecodeError, OSError):
            return []

    # --------------------------------------------------------
    # SAVE HISTORY
    # --------------------------------------------------------

    def save_history(self, history):
        """Save history to the JSON file."""

        with open(
            self.history_file,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                history,
                file,
                indent=4
            )

    # --------------------------------------------------------
    # ADD RECORD
    # --------------------------------------------------------

    def add_record(
        self,
        operation,
        pdf_count,
        total_pages,
        output_file,
        protected
    ):
        """Add a new operation to history."""

        history = self.load_history()

        record = {
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "operation": operation,
            "pdf_count": pdf_count,
            "total_pages": total_pages,
            "output_file": output_file,
            "protected": protected
        }

        history.append(record)

        self.save_history(history)

        return record

    # --------------------------------------------------------
    # GET HISTORY
    # --------------------------------------------------------

    def get_history(self):
        """Return all saved history records."""

        return self.load_history()

    # --------------------------------------------------------
    # CLEAR HISTORY
    # --------------------------------------------------------

    def clear_history(self):
        """Delete all history records."""

        self.save_history([])

    # --------------------------------------------------------
    # COUNT OPERATIONS
    # --------------------------------------------------------

    def get_operation_count(self):
        """Return the number of recorded operations."""

        return len(self.load_history())