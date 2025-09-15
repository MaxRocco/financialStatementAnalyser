import tkinter as tk
from tkinter import scrolledtext, messagebox
from fileOpening import select_file
from dataParsing import parse_excel, parse_pdf


class FinancialStatementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Statement Analysis")
        self.root.geometry("800x600")

        self.input = tk.Button(root, text="Upload File", command=self.upload_file)
        self.input.pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
        self.output.pack(padx=10, pady=10)

    def upload_file(self):
        filePath, fileType = select_file()

        if not filePath:
            messagebox.showinfo("No File", "You did not select a file.")
            return

        self.output.delete("1.0", tk.END)  # Todo: Test this

        if fileType == "Excel":
            dataFile = parse_excel(filePath)
            if dataFile is not None:
                self.output.insert(tk.END, f"Loaded Excel file: {filePath}\n\n")
                self.output.insert(tk.END, dataFile.head().to_string())  # Todo: Display data more elegantly for Excel
            else:
                self.output.insert(tk.END, "The Excel file could not be loaded successfully.")

        elif fileType == "PDF":
            text = parse_pdf(filePath)
            if text:
                self.output.insert(tk.END, f"Loaded PDF file: {filePath}\n\n")
                self.output.insert(tk.END, text[:5000])  # Todo: Display data more elegantly and specifically for PDF
            else:
                self.output.insert(tk.END, "The PDF File could not be loaded successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialStatementGUI(root)
    root.mainloop()
