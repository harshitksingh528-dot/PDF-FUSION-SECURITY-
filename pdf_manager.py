# ============================================================
# PDF Fusion & Security Manager
# File: pdf_manager.py
# Purpose: Main PDF processing engine
# ============================================================

import os

from pypdf import PdfWriter

from pdf_validator import PDFValidator
from pdf_info import PDFInfo
from pdf_security import PDFSecurity


class PDFManager:
    """
    Main manager for PDF selection, ordering,
    merging and security.
    """

    def __init__(self):
        """Initialize an empty PDF list."""
        self.selected_files = []

    # --------------------------------------------------------
    # ADD PDF
    # --------------------------------------------------------

    def add_pdf(self, file_path):
        """Validate and add a PDF to the list."""

        # Validate PDF
        validation = PDFValidator.validate_pdf(file_path)

        if not validation["valid"]:
            raise ValueError(validation["message"])

        # Prevent duplicate files
        if file_path in self.selected_files:
            raise ValueError(
                "This PDF has already been added."
            )

        self.selected_files.append(file_path)

        return True

    # --------------------------------------------------------
    # REMOVE PDF
    # --------------------------------------------------------

    def remove_pdf(self, index):
        """Remove a PDF using its position."""

        if index < 0 or index >= len(self.selected_files):
            raise IndexError(
                "Invalid PDF selection."
            )

        return self.selected_files.pop(index)

    # --------------------------------------------------------
    # MOVE PDF UP
    # --------------------------------------------------------

    def move_up(self, index):
        """Move a PDF one position upward."""

        if index <= 0:
            return False

        if index >= len(self.selected_files):
            raise IndexError(
                "Invalid PDF selection."
            )

        self.selected_files[index - 1], self.selected_files[index] = (
            self.selected_files[index],
            self.selected_files[index - 1]
        )

        return True

    # --------------------------------------------------------
    # MOVE PDF DOWN
    # --------------------------------------------------------

    def move_down(self, index):
        """Move a PDF one position downward."""

        if index < 0 or index >= len(self.selected_files) - 1:
            return False

        self.selected_files[index], self.selected_files[index + 1] = (
            self.selected_files[index + 1],
            self.selected_files[index]
        )

        return True

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------

    def clear(self):
        """Remove all selected PDFs."""

        self.selected_files.clear()

    # --------------------------------------------------------
    # TOTAL PAGES
    # --------------------------------------------------------

    def get_total_pages(self):
        """Return the total number of pages."""

        total_pages = 0

        for file_path in self.selected_files:
            info = PDFInfo.get_info(file_path)
            total_pages += info["page_count"]

        return total_pages

    # --------------------------------------------------------
    # PDF COUNT
    # --------------------------------------------------------

    def get_pdf_count(self):
        """Return the number of selected PDFs."""

        return len(self.selected_files)

    # --------------------------------------------------------
    # MERGE
    # --------------------------------------------------------

    def merge(self, output_file):
        """
        Merge all selected PDFs into one PDF.
        """

        if not self.selected_files:
            raise ValueError(
                "No PDFs have been selected."
            )

        writer = PdfWriter()

        for file_path in self.selected_files:

            if not os.path.exists(file_path):
                raise FileNotFoundError(
                    f"File not found: {file_path}"
                )

            writer.append(file_path)

        with open(output_file, "wb") as output:
            writer.write(output)

        return output_file

    # --------------------------------------------------------
    # MERGE + PROTECT
    # --------------------------------------------------------

    def merge_and_protect(
        self,
        output_file,
        password
    ):
        """
        Merge selected PDFs and then
        password-protect the final PDF.
        """

        if not self.selected_files:
            raise ValueError(
                "No PDFs have been selected."
            )

        # Temporary merged PDF
        temporary_file = "temporary_merged.pdf"

        try:

            # Step 1: Merge
            self.merge(temporary_file)

            # Step 2: Protect
            PDFSecurity.protect(
                temporary_file,
                output_file,
                password
            )

        finally:

            # Remove temporary file
            if os.path.exists(temporary_file):
                os.remove(temporary_file)

        return output_file