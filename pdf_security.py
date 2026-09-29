# ============================================================
# PDF Fusion & Security Manager
# File: pdf_security.py
# Purpose: Password-protect PDF files
# ============================================================

import os
from pypdf import PdfReader, PdfWriter

from config import MIN_PASSWORD_LENGTH


class PDFSecurity:
    """Handles PDF password protection."""

    @staticmethod
    def protect(input_file, output_file, password):
        """
        Encrypt a PDF using the supplied password.

        Parameters:
            input_file  : Path of the input PDF
            output_file : Path of the protected PDF
            password    : Password used for encryption

        Returns:
            Path of the protected PDF
        """

        # Check input file
        if not input_file:
            raise ValueError("Input PDF was not provided.")

        if not os.path.exists(input_file):
            raise FileNotFoundError(
                f"PDF not found: {input_file}"
            )

        if not input_file.lower().endswith(".pdf"):
            raise ValueError(
                "Input file must be a PDF."
            )

        # Check password
        if not password:
            raise ValueError(
                "Password cannot be empty."
            )

        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValueError(
                f"Password must contain at least "
                f"{MIN_PASSWORD_LENGTH} characters."
            )

        # Read the original PDF
        reader = PdfReader(input_file)

        # Create a new PDF writer
        writer = PdfWriter()

        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)

        # Encrypt PDF
        writer.encrypt(password)

        # Create protected PDF
        with open(output_file, "wb") as output:
            writer.write(output)

        return output_file