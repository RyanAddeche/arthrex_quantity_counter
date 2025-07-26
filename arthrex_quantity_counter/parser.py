import pdfplumber

from .sorter import find_file_path
from .utils import find_string
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

            # ID and Date are next to each other in the string when the pdf is parsed so they are found using the same find_string function then split
            # ID and Date grouped together are referenced as "info"
            info_start_marker = "Inventory Request ID Date"
            info_end_marker = "Comments"
            info = find_string(text, info_start_marker, info_end_marker)
            info = info.strip()
            inventoryID, date = info.split(' ', maxsplit=1)

            # Find all comments in the PDF
            comments_start_marker = "Comments"
            comments_end_marker = "Implants"
            comments = find_string(text, comments_start_marker, comments_end_marker)
            comments = comments.strip()
            comment_list = comments.split('\n')

            return text, warehouse, inventoryID, date, comment_list

    except Exception as e:
        print(f"Failed to read {target_pdf}: {e}")

def table_extraction_parser():
    targetPDF = find_file_name()
    try:
        words = []
        with pdfplumber.open(targetPDF) as pdf:
            for num in range(len(pdf.pages)):
                page = pdf.pages[num]
                words = words + page.extract_words()
            for word in words:
                print(word)

    except Exception as e:
        print(f"Failed to read {targetPDF}: {e}")



