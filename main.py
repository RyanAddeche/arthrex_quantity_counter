from io import BytesIO

from arthrex_quantity_counter.parser import text_parser, table_parser
from arthrex_quantity_counter.sorter import find_file_in_path, sort_file
from arthrex_quantity_counter.config import PDF_INPUT_DIR, PDF_OUTPUT_DIR

def main():

    file_path = find_file_in_path(PDF_INPUT_DIR)
    target_pdf_list = []

    unclean_implant_list = []
    unclean_instrument_list = []
    implant_list = []
    instrument_list = []
    for pdf in file_path:
        with open(pdf, 'rb') as f:
            pdf_bytes = f.read()
            target_pdf_list.append(BytesIO(pdf_bytes))

        warehouse, text = text_parser(pdf)
        print(warehouse)

        implant_identifier =  ['Implants', None, None, '', '', None, '', None, '']
        instrument_identifier = ['Instruments', None, None, '', '', None, '', None, '']
        cut_off_table_identifier = ['', 'Reference', 'Description', 'Qty', 'Target Qty']



        is_implant_table = False
        is_instrument_table = False

        table_list = table_parser(pdf)
        
        for table in table_list:
            for list in table:
                if list[0] == implant_identifier:
                    is_implant_table = True
                    is_instrument_table = False
                    del list[0]
                    del list[0]
                    for item in list:
                        unclean_implant_list.append(item)

                if list[0] == instrument_identifier:
                    is_implant_table = False
                    is_instrument_table = True
                    del list[0]
                    del list[0]
                    for item in list:
                        unclean_instrument_list.append(item)

                if list[0] == cut_off_table_identifier:
                    if is_implant_table:
                        del list[0]
                        for item in list:
                            unclean_implant_list.append(item)
                    if is_instrument_table:
                        del list[0]
                        for item in list:
                            unclean_instrument_list.append(item)
    print(unclean_implant_list)
    print("\n")
    print(unclean_instrument_list)


                    

                




    # output_dir = PDF_OUTPUT_DIR + warehouse
    # sort_file(file_path, output_dir)



if __name__ == "__main__":
    main()