# import_test.py
import cx_Oracle
import csv

con = cx_Oracle.connect('')
cur = con.cursor()
with open(r"csv_data_pipeline\data\output files\dataset.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for lines in csv_reader:
        cur.execute("insert into py (YEAR1, INDUSTRY_AGGREGATION_NZSIOC, INDUSTRY_CODE_NZSIOC, INDUSTRY_NAME_NZSIOC, UNITS, VARIABLE_CODE, VARIABLE_NAME, VARIABLE_CATEGORY, VALUE) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)",
            (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8]))
cur.close()
con.commit()
con.close()

print('Data load Success......Partyyyyy........')
