import os
import glob
import shutil

# Creates a list of all the pdfs inside a given directory
def find_file_in_path(dir):
    try:
        pdf_list = glob.glob(os.path.join(dir, '*.pdf'))
        if pdf_list:
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

def clean_list(unclean_list):
    new_list = []
    for row in unclean_list:
        try:
            id_part = row[0]
            qty_part = row[7]
            while (id_part[0].isdigit() or id_part[0] == ' '):
                id_part = id_part[1:]
            new_list.append([id_part, qty_part])
        except IndexError:
            id_part = row[0]
            id_part = id_part[2:]
            qty_part = row[-1]
            new_list.append([id_part, qty_part])
    return new_list
    
def combine_by_id(data):
    combined = {}
    for row in data:
        if len(row) < 2:
            continue  # skip malformed rows
        id_, qty = row[0], row[1]
        if qty is None:
            qty = '0'
        try:
            qty = int(qty)
        except ValueError:
            qty = 0  # fallback if qty can't convert
        combined[id_] = combined.get(id_, 0) + qty

    # Convert back to list of [id, total_qty]
    return [[id_, str(total_qty)] for id_, total_qty in combined.items()]



