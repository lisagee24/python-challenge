import os

import csv

csvpath = "../PyBank/Resources/"

budget_dataFile = os.path.join(csvpath,"budget_data.csv")



with open(csvpath, newline = ' ') as budget_data.csv: 
    budget_dataReader = budget_data.Reader(budget_data.csv, delimiter = ',')
    print (budget_dataReader)
for row in budget_dataReader:
    print(row)