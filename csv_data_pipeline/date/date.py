from datetime import date   #extract only date from datetime function
import os

#changing the default directory to another path
os.chdir(r'C:\Users\sathegde\Desktop\test')
#date.today display the current sysdate
today = str(date.today())
#list all the files from current directory i.e C:\Users\sathegde\Desktop\test
for filename in os.listdir('.'):
    #check all the files in directory which ends with .csv
    if filename.endswith('.csv'):
        #os.rename(actual_name,new_name) changes to new name
        os.rename(filename,today+'.csv')
        #prints success if renamed 
        print("success")
