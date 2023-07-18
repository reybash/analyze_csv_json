import csv

filename = 'data/san_francisco.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    
    for index, column_header in enumerate(header_row):
        print("Column {}: {}".format(index,column_header))