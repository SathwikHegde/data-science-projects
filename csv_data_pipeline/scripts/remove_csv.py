import os
path = (r'csv_data_pipeline\data\output files\dataset.csv')
extension = '.csv'

for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
            os.remove(file_name_path)
            print('File removed :',file_name )
        else:
            print('File not removed')
