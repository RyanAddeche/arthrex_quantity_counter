import os
import glob
import shutil



#os.rename("placeToSort/file.foo", "path/to/new/destination/for/file.foo")

def find_file_path(dir):
    try:
        pdf_path = glob.glob(os.path.join(dir, '*.pdf'))

        if pdf_path:
            return pdf_path[0]
        else:
            print("No PDF files found in the specified folder.")
    except Exception as e:
        print(f"An error occurred: {e}")


def sort_file(input_file_loc, output_file_loc):
    if not os.path.exists(output_file_loc):
        os.makedirs(output_file_loc)

    try:
        shutil.move(input_file_loc, output_file_loc)
    except FileNotFoundError:
        print(f"Error: Source file not found at '{input_file_loc}'")
    except Exception as e:
        print(f"An error occurred: {e}")



