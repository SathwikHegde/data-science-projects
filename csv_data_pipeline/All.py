import os
import glob
import fnmatch
import csv
import ctypes
from datetime import date
from shutil import copy2

SOURCE_DIR = r"csv_data_pipeline\data\source files"
DEST_DIR = r"csv_data_pipeline\data\output files"

def remove_old_csvs(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.csv'):
                os.remove(os.path.join(root, file))
                print(f"Removed: {file}")

def copy_csv_files(source, destination):
    os.makedirs(destination, exist_ok=True)
    for file in glob.iglob(os.path.join(source, "*.csv")):
        if os.path.isfile(file):
            copy2(file, destination)
            print(f"Copied: {os.path.basename(file)}")

def rename_csv_files(path):
    today_str = str(date.today())
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            new_name = os.path.join(path, today_str + '.csv')
            os.rename(os.path.join(path, filename), new_name)
            print(f"Renamed to: {new_name}")
            break

def count_rows(path):
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, '*.csv'):
            with open(os.path.join(path, file), 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                row_count = sum(1 for _ in reader)
            print(f"Rows in {file}: {row_count}")
            ctypes.windll.user32.Message
