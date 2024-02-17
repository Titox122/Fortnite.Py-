#Script By Project164
import os
import sys
import shutil

def convert_ufont_to_otf(file_paths):
    for file_path in file_paths:
        if file_path.endswith('.ufont'):
            output_file_path = os.path.splitext(file_path)[0] + '.otf'
           
            shutil.copy(file_path, output_file_path)
            print(f"Converted '{file_path}' To '{output_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drag The Ufonts")
    else:
        file_paths = sys.argv[1:]
        convert_ufont_to_otf(file_paths)
