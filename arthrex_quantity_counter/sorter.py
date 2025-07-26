import os
import glob
import shutil

# Creates a list of all the pdfs inside a given directory
def find_file_in_path(dir):
    try:
        pdf_list = glob.glob(os.path.join(dir, '*.pdf'))
        if pdf_list:
            for pdf in pdf_list:
                print(pdf)
            return pdf_list
        else:
            print("No PDF files found in the specified folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Moves a file to a new directory
def sort_file(input_file_loc, output_file_loc):
    if not os.path.exists(output_file_loc):
        os.makedirs(output_file_loc)

    try:
        shutil.move(input_file_loc, output_file_loc)
    except FileNotFoundError:
        print(f"Error: Source file not found at '{input_file_loc}'")
    except Exception as e:
        print(f"An error occurred: {e}")



