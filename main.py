from fileOpening import select_file
from dataParsing import parse_excel, parse_pdf


def main():
    file_path, file_type = select_file()

    if not file_path:
        print("You did not select a file.")
        return

    if file_type == "Excel":
        dataFile = parse_excel(file_path)
        if dataFile is not None:
            print("Excel data: ")
            print(dataFile.head())  # Todo: Implement a way to print specific information, fix presentation
            # Todo: Remove redundancy; do not display NaN values in cells that are just empty
        else:
            print("Failed to parse Excel file.")

    elif file_type == "PDF":
        text = parse_pdf(file_path)
        if text:
            print("PDF text: ")
            print(text[:500])  # Todo: Implement a way to print specific information, fix presentation
        else:
            print("Failed to parse PDF.")


if __name__ == "__main__":
    main()
