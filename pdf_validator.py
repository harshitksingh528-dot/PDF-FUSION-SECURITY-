# ============================================================
# PDF Fusion & Security Manager
# File: pdf_validator.py
# Purpose: Validate PDF files before processing
# ============================================================

import os
from pypdf import PdfReader


class PDFValidator:
    """Provides validation functions for PDF files."""

    @staticmethod
    def validate_path(file_path):
        """
        Check whether the selected path exists
        and has a PDF extension.
        """

        if not file_path:
            raise ValueError("No file was selected.")

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if not os.path.isfile(file_path):
            raise ValueError(
                f"The selected path is not a file: {file_path}"
            )

        if not file_path.lower().endswith(".pdf"):
            raise ValueError(
                f"Not a PDF file: {file_path}"
            )

        return True

    @staticmethod
    def validate_pdf(file_path):
        """
        Check whether the file is a readable PDF.
        """

        # First validate the path
        PDFValidator.validate_path(file_path)

        try:
            reader = PdfReader(file_path)

            # Check if PDF is encrypted
            if reader.is_encrypted:
                return {
                    "valid": False,
                    "encrypted": True,
                    "message": "PDF is password protected."
                }

            # Try accessing the pages
            page_count = len(reader.pages)

            if page_count == 0:
                return {
                    "valid": False,
                    "encrypted": False,
                    "message": "PDF contains no pages."
                }

            return {
                "valid": True,
                "encrypted": False,
                "page_count": page_count,
                "message": "Valid PDF."
            }

        except Exception as error:
            return {
                "valid": False,
                "encrypted": False,
                "message": f"Invalid or corrupted PDF: {error}"}