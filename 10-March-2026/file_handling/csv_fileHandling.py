import csv
from datetime import date

file = open('expense.csv','a+', newline = '')
# w = csv.writer(file)
r = csv.reader(file)
file.seek(0)
print(list(r))

# w.writerow([ 'DATE', 'CATEGORY', 'AMOUNT' ]) ## Column name
# w.writerows(
#     [
#         [date.today(),'Tarvel', 2000],
#         [date.today(),'Food', 200],
#         [date.today(),'Sleeping', 15000],
#         [date.today(),'Entertainment', 8000]
#     ]
# )

file.close()