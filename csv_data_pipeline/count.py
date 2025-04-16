import os
import fnmatch
import csv
import ctypes

def count_csv_rows(directory):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return
    for file in os.listdir(directory):
        if fnmatch.fnmatch(file, '*.csv'):
            with open(os.path.join(directory, file), 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                row_count = sum(1 for _ in reader)
            print(f"Rows in {file}: {row_count}")
            ctypes.windll.user32.MessageBoxW(0, f"Number of Rows: {row_count}", "Row Count", 1)

if __name__ == "__main__":
    target_dir = r"D:\copy"
    count_csv_rows(target_dir)
