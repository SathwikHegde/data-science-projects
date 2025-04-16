import subprocess
import glob
import os
from shutil import copy2

def run_sqlldr():
    cmd = 'sqlldr userid= control=csv_data_pipeline\config\control.ctl'
    subprocess.call(cmd, shell=True)
    print("Data loaded successfully")

def archive_csv(source_dir, archive_dir):
    os.makedirs(archive_dir, exist_ok=True)
    for file in glob.iglob(os.path.join(source_dir, "*.csv")):
        if os.path.isfile(file):
            copy2(file, archive_dir)
            print("Archived:", os.path.basename(file))

if __name__ == "__main__":
    run_sqlldr()
    archive_csv(r"csv_data_pipeline\data\output files")

    


