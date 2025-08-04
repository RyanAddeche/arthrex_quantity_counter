import pdfplumber

from .sorter import find_file_in_path
from .config import WAREHOUSE_INFO

def text_parser(target_pdf):
    try:
        with pdfplumber.open(target_pdf) as pdf:

            # Parses file and generates string of text for the entire pdf
            text = ""
            for num in range(len(pdf.pages)):
                page = pdf.pages[num]
                text = text + page.extract_text()

            # Checks each warehouse name from pdf to find the correct warehouse, returns warehouse name
            warehouse = ""
            for sublist in WAREHOUSE_INFO:
                if sublist[1] in text:
                    warehouse = sublist[0]

            return warehouse, text

    except Exception as e:
        print(f"Failed to read {target_pdf}: {e}")

def table_parser(target_pdf):
    try:
        table_list = []
        with pdfplumber.open(target_pdf) as pdf:

            pdf_filename = (pdf.stream.name)

            for num in range(len(pdf.pages)):
                page = pdf.pages[num]
                table_list.append(page.extract_tables())
            return table_list, pdf_filename

    except Exception as e:
        print(f"Failed to read {target_pdf}: {e}")



