import csv
input_file = open(r"C:\Users\sathegde\Desktop\test\2018-07-31.csv","r+")
reader_file = csv.reader(input_file)
value = (len(list(reader_file))-1)
print(value)