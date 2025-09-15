import pandas as pd
import fitz  # This is PyMuPDF, see CREDITS.md


def parse_excel(filePath):
    try:
        dataFile = pd.read_excel(filePath)
        return dataFile
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None


def parse_pdf(filePath):
    try:
        text = ""
        with fitz.open(filePath) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
