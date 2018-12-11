import csv

datas = [['name', 'age'],
         ['Bob', 14],
         ['Tom', 23],
         ['Jerry', '18']]

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(datas)