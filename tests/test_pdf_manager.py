# ============================================================
# PDF Fusion & Security Manager
# File: tests/test_pdf_manager.py
# Purpose: Automated tests for PDF processing
# ============================================================

import os
import tempfile
import unittest

from pypdf import PdfReader, PdfWriter

from pdf_manager import PDFManager


class TestPDFManager(unittest.TestCase):

    def setUp(self):
        """Create temporary PDF files for testing."""

        self.test_folder = tempfile.mkdtemp()

        self.pdf1 = os.path.join(
            self.test_folder,
            "test1.pdf"
        )

        self.pdf2 = os.path.join(
            self.test_folder,
            "test2.pdf"
        )

        self.create_pdf(self.pdf1, 2)
        self.create_pdf(self.pdf2, 3)

        self.manager = PDFManager()

    # --------------------------------------------------------
    # CREATE TEST PDF
    # --------------------------------------------------------

    def create_pdf(self, path, pages):
        """Create a simple PDF for testing."""

        writer = PdfWriter()

        for _ in range(pages):
            writer.add_blank_page(
                width=595,
                height=842
            )

        with open(path, "wb") as file:
            writer.write(file)

    # --------------------------------------------------------
    # TEST ADD
    # --------------------------------------------------------

    def test_add_pdf(self):

        self.manager.add_pdf(self.pdf1)

        self.assertEqual(
            self.manager.get_pdf_count(),
            1
        )

    # --------------------------------------------------------
    # TEST TOTAL PAGES
    # --------------------------------------------------------

    def test_total_pages(self):

        self.manager.add_pdf(self.pdf1)
        self.manager.add_pdf(self.pdf2)

        self.assertEqual(
            self.manager.get_total_pages(),
            5
        )

    # --------------------------------------------------------
    # TEST REMOVE
    # --------------------------------------------------------

    def test_remove_pdf(self):

        self.manager.add_pdf(self.pdf1)
        self.manager.add_pdf(self.pdf2)

        self.manager.remove_pdf(0)

        self.assertEqual(
            self.manager.get_pdf_count(),
            1
        )

    # --------------------------------------------------------
    # TEST REORDER
    # --------------------------------------------------------

    def test_reorder(self):

        self.manager.add_pdf(self.pdf1)
        self.manager.add_pdf(self.pdf2)

        self.manager.move_down(0)

        self.assertEqual(
            self.manager.selected_files[0],
            self.pdf2
        )

    # --------------------------------------------------------
    # TEST MERGE
    # --------------------------------------------------------

    def test_merge(self):

        self.manager.add_pdf(self.pdf1)
        self.manager.add_pdf(self.pdf2)

        output = os.path.join(
            self.test_folder,
            "merged.pdf"
        )

        self.manager.merge(output)

        self.assertTrue(
            os.path.exists(output)
        )

        reader = PdfReader(output)

        self.assertEqual(
            len(reader.pages),
            5
        )

    # --------------------------------------------------------
    # TEST MERGE + PROTECT
    # --------------------------------------------------------

    def test_merge_and_protect(self):

        self.manager.add_pdf(self.pdf1)
        self.manager.add_pdf(self.pdf2)

        output = os.path.join(
            self.test_folder,
            "protected.pdf"
        )

        self.manager.merge_and_protect(
            output,
            "Test1234"
        )

        self.assertTrue(
            os.path.exists(output)
        )

        reader = PdfReader(output)

        self.assertTrue(
            reader.is_encrypted
        )

    # --------------------------------------------------------
    # CLEANUP
    # --------------------------------------------------------

    def tearDown(self):
        """Remove temporary test files."""

        for filename in os.listdir(
            self.test_folder
        ):
            file_path = os.path.join(
                self.test_folder,
                filename
            )

            if os.path.isfile(file_path):
                os.remove(file_path)

        os.rmdir(self.test_folder)


# ============================================================
# RUN TESTS
# ============================================================

if __name__ == "__main__":
    unittest.main()