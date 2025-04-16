import os

def check_csv_exists(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                print(f"CSV exists: {file}")
                return
    print("No CSV file exists")

if __name__ == "__main__":
    path = r"csv_data_pipeline\data\source files"
    check_csv_exists(path)
