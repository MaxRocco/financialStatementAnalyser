import tkinter as tk
from tkinter import filedialog, messagebox
import os


def select_file():
    while True:
        root = tk.Tk()
        root.withdraw()

        filePath = filedialog.askopenfilename(
            title="Select a Financial Statement",
            filetypes=[("Excel or PDF files", "*.xlsx *.xls *.pdf")]
        )

        if not filePath:
            retry = messagebox.askyesno("No File Selected", "You did not select a file. Try again?")
            if not retry:
                return None, None
            continue

        extension = os.path.splitext(filePath)[1].lower()

        if extension in [".xlsx", ".xls"]:
            fileType = "Excel"
        elif extension == ".pdf":
            fileType = "PDF"
        else:
            messagebox.showerror("Unsupported File")
            continue

        return filePath, fileType


file_path, file_type = select_file()

if file_path:
    if file_type == "Excel":
        print("Excel file loaded")
    elif file_type == "PDF":
        print("PDF file loaded")
