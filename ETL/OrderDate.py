import pyodbc
import os
import csv

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = '''
SELECT sales_order.id, Day([order_date]) AS [day], Month([order_date]) AS [month], IIf(Month([order_date])<=3,1,IIf(Month([order_date])<=6,2,IIf(Month([order_date])<=9,3,4))) AS quarter, Year([order_date]) AS [year]
FROM sales_order
WHERE (((IsDate([order_date]))<>False));
'''
cursor.execute(query)
results = cursor.fetchall()

# Create a directory to store the data
if not os.path.exists('Output'):
    os.makedirs('Output')

with open('Output/OrderDate.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['ID', 'Day', 'Month', 'Quarter', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow({'ID': row[0], 'Day': row[1], 'Month': row[2], 'Quarter': row[3], 'Year': row[4]})
