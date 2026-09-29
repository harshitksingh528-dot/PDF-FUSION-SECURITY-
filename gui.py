# ============================================================
# PDF Fusion & Security Manager
# File: gui.py
# Purpose: Graphical User Interface
# ============================================================

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from config import (
    APP_TITLE,
    DEFAULT_OUTPUT_FILE,
    MAX_PDF_FILES,
    MIN_PASSWORD_LENGTH,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

from pdf_manager import PDFManager
from pdf_info import PDFInfo
from history_manager import HistoryManager


class PDFFusionApp:
    """Main graphical interface for the application."""

    def __init__(self, root):
        self.root = root

        self.root.title(APP_TITLE)
        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )
        self.root.minsize(850, 600)

        # Main processing manager
        self.manager = PDFManager()

        # History manager
        self.history = HistoryManager()

        self.create_gui()

    # ========================================================
    # GUI CREATION
    # ========================================================

    def create_gui(self):

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        title = tk.Label(
            self.root,
            text="PDF FUSION & SECURITY MANAGER",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=(15, 5))

        subtitle = tk.Label(
            self.root,
            text="Merge, arrange and password-protect PDF files",
            font=("Arial", 11)
        )

        subtitle.pack(pady=(0, 15))

        # ----------------------------------------------------
        # MAIN FRAME
        # ----------------------------------------------------

        main_frame = tk.Frame(self.root)

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ----------------------------------------------------
        # LEFT PANEL
        # ----------------------------------------------------

        left_frame = tk.LabelFrame(
            main_frame,
            text="Selected PDF Files",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # Listbox
        self.pdf_listbox = tk.Listbox(
            left_frame,
            font=("Arial", 11),
            selectmode=tk.SINGLE
        )

        self.pdf_listbox.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            left_frame,
            orient="vertical",
            command=self.pdf_listbox.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.pdf_listbox.config(
            yscrollcommand=scrollbar.set
        )

        # ----------------------------------------------------
        # BUTTON PANEL
        # ----------------------------------------------------

        button_frame = tk.Frame(left_frame)

        button_frame.pack(
            fill="x",
            pady=(10, 0)
        )

        tk.Button(
            button_frame,
            text="Add PDF",
            command=self.add_pdf,
            width=12
        ).grid(row=0, column=0, padx=3, pady=3)

        tk.Button(
            button_frame,
            text="Remove",
            command=self.remove_pdf,
            width=12
        ).grid(row=0, column=1, padx=3, pady=3)

        tk.Button(
            button_frame,
            text="Move Up",
            command=self.move_up,
            width=12
        ).grid(row=1, column=0, padx=3, pady=3)

        tk.Button(
            button_frame,
            text="Move Down",
            command=self.move_down,
            width=12
        ).grid(row=1, column=1, padx=3, pady=3)

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_files,
            width=12
        ).grid(row=2, column=0, padx=3, pady=3)

        tk.Button(
            button_frame,
            text="Show Details",
            command=self.show_pdf_details,
            width=12
        ).grid(row=2, column=1, padx=3, pady=3)

        # ----------------------------------------------------
        # RIGHT PANEL
        # ----------------------------------------------------

        right_frame = tk.Frame(main_frame)

        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # INFORMATION PANEL
        # ----------------------------------------------------

        info_frame = tk.LabelFrame(
            right_frame,
            text="PDF Information",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        info_frame.pack(
            fill="both",
            expand=True
        )

        self.info_text = tk.Text(
            info_frame,
            height=10,
            width=40,
            font=("Consolas", 10),
            state="disabled"
        )

        self.info_text.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # PASSWORD PANEL
        # ----------------------------------------------------

        security_frame = tk.LabelFrame(
            right_frame,
            text="PDF Security",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        security_frame.pack(
            fill="x",
            pady=(10, 0)
        )

        tk.Label(
            security_frame,
            text="Password:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.password_entry = tk.Entry(
            security_frame,
            show="*",
            width=30
        )

        self.password_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            security_frame,
            text="Confirm:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.confirm_password_entry = tk.Entry(
            security_frame,
            show="*",
            width=30
        )

        self.confirm_password_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # ----------------------------------------------------
        # OUTPUT FILE
        # ----------------------------------------------------

        output_frame = tk.LabelFrame(
            right_frame,
            text="Output",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        output_frame.pack(
            fill="x",
            pady=(10, 0)
        )

        self.output_entry = tk.Entry(
            output_frame,
            width=40
        )

        self.output_entry.insert(
            0,
            DEFAULT_OUTPUT_FILE
        )

        self.output_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Button(
            output_frame,
            text="Browse",
            command=self.choose_output
        ).pack(
            side="right",
            padx=(5, 0)
        )

        # ----------------------------------------------------
        # PROCESS BUTTON
        # ----------------------------------------------------

        self.process_button = tk.Button(
            right_frame,
            text="MERGE & PROTECT PDF",
            command=self.process_pdf,
            font=("Arial", 13, "bold"),
            height=2
        )

        self.process_button.pack(
            fill="x",
            pady=15
        )

        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        self.status_var = tk.StringVar()

        self.status_var.set(
            "Ready. Add PDF files to begin."
        )

        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            relief="sunken",
            padx=10
        )

        status_label.pack(
            side="bottom",
            fill="x"
        )

    # ========================================================
    # ADD PDF
    # ========================================================

    def add_pdf(self):

        if self.manager.get_pdf_count() >= MAX_PDF_FILES:
            messagebox.showwarning(
                "Limit Reached",
                f"You can select a maximum of "
                f"{MAX_PDF_FILES} PDFs."
            )
            return

        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[
                ("PDF files", "*.pdf")
            ]
        )

        if not files:
            return

        added = 0

        for file_path in files:

            try:
                self.manager.add_pdf(file_path)
                added += 1

            except Exception as error:

                messagebox.showerror(
                    "PDF Error",
                    f"{os.path.basename(file_path)}\n\n"
                    f"{error}"
                )

        self.refresh_list()

        self.status_var.set(
            f"{added} PDF(s) added."
        )

    # ========================================================
    # REMOVE PDF
    # ========================================================

    def remove_pdf(self):

        selection = self.pdf_listbox.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a PDF to remove."
            )
            return

        index = selection[0]

        self.manager.remove_pdf(index)

        self.refresh_list()

        self.status_var.set(
            "PDF removed."
        )

    # ========================================================
    # MOVE UP
    # ========================================================

    def move_up(self):

        selection = self.pdf_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        if self.manager.move_up(index):

            self.refresh_list()

            self.pdf_listbox.selection_set(
                index - 1
            )

            self.status_var.set(
                "PDF moved up."
            )

    # ========================================================
    # MOVE DOWN
    # ========================================================

    def move_down(self):

        selection = self.pdf_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        if self.manager.move_down(index):

            self.refresh_list()

            self.pdf_listbox.selection_set(
                index + 1
            )

            self.status_var.set(
                "PDF moved down."
            )

    # ========================================================
    # CLEAR
    # ========================================================

    def clear_files(self):

        if not self.manager.selected_files:
            return

        answer = messagebox.askyesno(
            "Clear PDFs",
            "Remove all selected PDFs?"
        )

        if answer:

            self.manager.clear()

            self.refresh_list()

            self.clear_information()

            self.status_var.set(
                "All PDFs removed."
            )

    # ========================================================
    # REFRESH LIST
    # ========================================================

    def refresh_list(self):

        self.pdf_listbox.delete(
            0,
            tk.END
        )

        for index, file_path in enumerate(
            self.manager.selected_files,
            start=1
        ):

            file_name = os.path.basename(
                file_path
            )

            self.pdf_listbox.insert(
                tk.END,
                f"{index}. {file_name}"
            )

    # ========================================================
    # SHOW DETAILS
    # ========================================================

    def show_pdf_details(self):

        selection = self.pdf_listbox.curselection()

        if not selection:

            self.clear_information()

            self.info_text.config(
                state="normal"
            )

            self.info_text.insert(
                tk.END,
                "Select a PDF to view its details."
            )

            self.info_text.config(
                state="disabled"
            )

            return

        index = selection[0]

        file_path = self.manager.selected_files[index]

        try:

            info = PDFInfo.get_info(
                file_path
            )

            details = (
                f"File Name : {info['file_name']}\n"
                f"File Size : {info['file_size_formatted']}\n"
                f"Pages     : {info['page_count']}\n"
                f"Encrypted : {info['encrypted']}\n"
                f"\nPath:\n{info['file_path']}"
            )

            self.info_text.config(
                state="normal"
            )

            self.info_text.delete(
                "1.0",
                tk.END
            )

            self.info_text.insert(
                tk.END,
                details
            )

            self.info_text.config(
                state="disabled"
            )

        except Exception as error:

            messagebox.showerror(
                "Information Error",
                str(error)
            )

    # ========================================================
    # CLEAR INFORMATION
    # ========================================================

    def clear_information(self):

        self.info_text.config(
            state="normal"
        )

        self.info_text.delete(
            "1.0",
            tk.END
        )

        self.info_text.config(
            state="disabled"
        )

    # ========================================================
    # CHOOSE OUTPUT
    # ========================================================

    def choose_output(self):

        file_path = filedialog.asksaveasfilename(
            title="Save Protected PDF",
            defaultextension=".pdf",
            filetypes=[
                ("PDF files", "*.pdf")
            ]
        )

        if file_path:

            self.output_entry.delete(
                0,
                tk.END
            )

            self.output_entry.insert(
                0,
                file_path
            )

    # ========================================================
    # PROCESS PDF
    # ========================================================

    def process_pdf(self):

        # Check PDF selection
        if not self.manager.selected_files:

            messagebox.showwarning(
                "No PDFs",
                "Please add at least one PDF."
            )

            return

        # Get passwords
        password = self.password_entry.get()
        confirm_password = (
            self.confirm_password_entry.get()
        )

        # Validate password
        if not password:

            messagebox.showwarning(
                "Password Required",
                "Please enter a password."
            )

            return

        if len(password) < MIN_PASSWORD_LENGTH:

            messagebox.showwarning(
                "Password Too Short",
                f"Password must contain at least "
                f"{MIN_PASSWORD_LENGTH} characters."
            )

            return

        if password != confirm_password:

            messagebox.showwarning(
                "Password Mismatch",
                "Passwords do not match."
            )

            return

        # Output path
        output_file = self.output_entry.get().strip()

        if not output_file:

            messagebox.showwarning(
                "Output Required",
                "Please select an output file."
            )

            return

        if not output_file.lower().endswith(".pdf"):
            output_file += ".pdf"

        try:

            self.process_button.config(
                state="disabled"
            )

            self.status_var.set(
                "Processing PDF..."
            )

            self.root.update_idletasks()

            # Merge and protect
            result = self.manager.merge_and_protect(
                output_file,
                password
            )

            # Collect information
            pdf_count = self.manager.get_pdf_count()
            total_pages = self.manager.get_total_pages()

            # Save history
            self.history.add_record(
                operation="Merge and Protect",
                pdf_count=pdf_count,
                total_pages=total_pages,
                output_file=result,
                protected=True
            )

            self.status_var.set(
                "PDF created successfully."
            )

            messagebox.showinfo(
                "Success",
                "PDF created successfully!\n\n"
                f"Output:\n{result}\n\n"
                f"PDFs merged: {pdf_count}\n"
                f"Total pages: {total_pages}"
            )

        except Exception as error:

            self.status_var.set(
                "Processing failed."
            )

            messagebox.showerror(
                "Processing Error",
                str(error)
            )

        finally:

            self.process_button.config(
                state="normal"
            )


# ============================================================
# APPLICATION START FUNCTION
# ============================================================

def launch_app():
    """Launch the PDF Fusion application."""

    root = tk.Tk()

    app = PDFFusionApp(root)

    root.mainloop()