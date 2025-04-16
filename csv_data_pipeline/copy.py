import os
import glob
from shutil import copy2

def copy_csv_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    files = glob.iglob(os.path.join(source_dir, "*.csv"))
    for file in files:
        if os.path.isfile(file):
            copy2(file, destination_dir)
            print(f"Copied: {os.path.basename(file)}")

if __name__ == "__main__":
    source = r"csv_data_pipeline\data\source files"
    destination = r"csv_data_pipeline\data\output files"
    
    copy_csv_files(source, destination)
