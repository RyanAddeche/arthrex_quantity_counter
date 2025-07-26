from io import BytesIO

from arthrex_quantity_counter.parser import text_parser
from arthrex_quantity_counter.sorter import find_file_path, sort_file
from arthrex_quantity_counter.config import PDF_INPUT_DIR, PDF_OUTPUT_DIR

def main():

    file_path = find_file_path(PDF_INPUT_DIR)
    with open(file_path, 'rb') as f:
        pdf_bytes = f.read()
        target_pdf = BytesIO(pdf_bytes)

    text, warehouse, inventoryID, date, comment_list = text_parser(target_pdf)
    print(text)
    print(warehouse, inventoryID, date, comment_list)

    output_dir = PDF_OUTPUT_DIR + warehouse
    sort_file(file_path, output_dir)



if __name__ == "__main__":
    main()