import fnmatch
import os
import csv
import ctypes
#the path of the directory
path= r'C:\Users\sathegde\Desktop\test'
# os.listdir function list all the files in the given path
for file in os.listdir(path):
    #fmatch matches all the files that end with .csv in the given path
    if fnmatch.fnmatch(file, '*.csv'):
        #Join one or more path and the return value is the concatenation of path
        #open(filename,mode) used to open the given file or path and read
        file_name_path = open(os.path.join(path,file), 'r+')
        #csv.reader used to read all lines from .csv file for the given path or file
        reader_file = csv.reader(file_name_path)
        #value returns the row count in csv file
        value = (len(list(reader_file)) - 1)
        #print the row count and file name
        print('\n No. Of. Rows in %s  is %d ' % (file, value))
        #print(f'\n No. Of. Rows in {file} is {value:d} ') another way to print
        #ctypes messagebox used to display result in a dialogue box 
        ctypes.windll.user32.MessageBoxW(0, "           Number of Rows : " + str(value), "Row Count", 1)
        #print (file)
        #print(value)
