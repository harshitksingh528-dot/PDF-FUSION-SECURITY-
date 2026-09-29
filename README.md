# PDF Fusion & Security Manager

## 1. Project Overview

PDF Fusion & Security Manager is a Python-based desktop application
designed to simplify PDF management.

The application allows users to:

- Select multiple PDF files
- Validate PDF files
- View PDF information
- Reorder PDF files
- Remove PDF files
- Merge multiple PDFs
- Password-protect the final PDF
- Maintain operation history

The project combines PDF processing and PDF security into one
user-friendly desktop application.

---

## 2. Problem Statement

Managing multiple PDF documents can become inconvenient when users
need to combine documents and protect the resulting file.

Users may need to:

- Combine several PDF files
- Control the order of pages
- Check PDF information
- Protect important documents with a password
- Keep track of previous operations

This project provides these functions through a single application.

---

## 3. Objectives

The main objectives are:

1. Develop a desktop application for PDF management.
2. Merge multiple PDF documents.
3. Allow users to arrange PDFs before merging.
4. Provide PDF validation and information.
5. Protect the final PDF using a password.
6. Maintain a history of completed operations.
7. Provide error handling and input validation.
8. Demonstrate modular Python programming.

---

## 4. Major Functional Modules

### Module 1 — PDF Validation

Validates selected PDF files before processing.

### Module 2 — PDF Information

Displays:

- File name
- File size
- Page count
- Encryption status

### Module 3 — PDF Processing

Allows users to:

- Add PDFs
- Remove PDFs
- Reorder PDFs
- Merge PDFs

### Module 4 — PDF Security

Protects the final PDF using password encryption.

### Module 5 — History Management

Stores information about completed operations.

### Module 6 — Graphical User Interface

Provides an easy-to-use desktop interface.

---

## 5. Non-Functional Requirements

The project considers the following requirements:

### Performance

PDF operations should complete efficiently for normal document sizes.

### Security

The application provides password protection for output PDFs.

### Usability

The graphical interface provides clear buttons, fields and messages.

### Reliability

Invalid files and incorrect inputs are handled using validation
and error messages.

### Maintainability

The application is divided into separate modules.

### Resource Efficiency

Temporary files are removed after processing.

---

## 6. Technologies Used

### Programming Language

Python

### GUI

Tkinter

### PDF Processing

pypdf

### Data Storage

JSON

### Testing

Python unittest

### Development Environment

Visual Studio Code

### Version Control

Git / GitHub

---

## 7. Project Structure

```text
PDF_Fusion_Security_Manager/
│
├── config.py
├── requirements.txt
├── pdf_validator.py
├── pdf_info.py
├── pdf_security.py
├── pdf_manager.py
├── history_manager.py
├── gui.py
├── main.py
│
└── tests/
    └── test_pdf_manager.py