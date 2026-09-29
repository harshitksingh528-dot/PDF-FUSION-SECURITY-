# ============================================================
# PDF Fusion & Security Manager
# File: pdf_info.py
# Purpose: Extract information from PDF files
# ============================================================

import os
from pypdf import PdfReader


class PDFInfo:
    """Provides information about PDF files."""

    @staticmethod
    def get_info(file_path):
        """
        Return important information about a PDF.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        reader = PdfReader(file_path)

        return {
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
            "file_size": os.path.getsize(file_path),
            "file_size_formatted": PDFInfo.format_size(
                os.path.getsize(file_path)
            ),
            "page_count": len(reader.pages),
            "encrypted": reader.is_encrypted
        }

    @staticmethod
    def format_size(size_bytes):
        """
        Convert bytes into a readable file size.
        """

        if size_bytes < 1024:
            return f"{size_bytes} B"

        if size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"

        if size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} MB"

        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"