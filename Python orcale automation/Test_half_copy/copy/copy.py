import glob
import os
from shutil import copy2

source_dir = (r'C:\Users\abmahali\Desktop\test') #Path where your files are at the moment
dst = (r'D:\copy') #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.csv"))
for file in files:
    if os.path.isfile(file):
        copy2(file, dst)
        print ('The CSV file %s  is successfuly copied' %(file))
    else:
         print("not success")
