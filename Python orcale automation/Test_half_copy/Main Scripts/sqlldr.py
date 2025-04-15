import subprocess
import glob
import os
from shutil import copy2

subprocess.call(r'sqlldr userid= control=C:\Users\sathegde\Desktop\test\control.ctl', shell=True)

print("Data Loaded into Database successfully")

source_dir = (r'C:\Users\sathegde\Desktop\test') #Path where your files are at the moment
dst = (r'C:\Users\sathegde\Desktop\test\archive') #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.csv"))
for file in files:
    if os.path.isfile(file):
        copy2(file, dst)
        print("File moved to archive folder")
    else:
         print("not success")
