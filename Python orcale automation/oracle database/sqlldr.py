import subprocess
import glob
import os
from shutil import copy2

subprocess.call(r'sqlldr userid=INTBZ/intbz12#$@206.245.13.25/HRBOTEST control=C:\Users\sathegde\Desktop\Python_auto\control.ctl', shell=True)

print("Data Loaded into Database successfully")

source_dir = (r'C:\Users\sathegde\Desktop\Python_auto') #Path where your files are at the moment
dst = (r'C:\Users\sathegde\Desktop\Python_auto\archive') #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.csv"))
for file in files:
    if os.path.isfile(file):
        copy2(file, dst)
        print("File moved to archive folder")
    else:
         print("not success")
