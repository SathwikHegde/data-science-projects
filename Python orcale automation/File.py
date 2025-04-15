import os
path = (r'C:\Users\sathegde\Desktop\test')
extension = '.csv'

for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
            print('The CSV file exists:',file_name )
        else:
            print('No CSV file exists')
