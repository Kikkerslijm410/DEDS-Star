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
SELECT product.name, product.category
FROM product;
'''
cursor.execute(query)
results = cursor.fetchall()

# Create a directory to store the data
if not os.path.exists('ETL/Output'):
    os.makedirs('ETL/Output')

with open('ETL/Output/Product.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['ProductID', 'Name', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    x = 1
    for row in results:
        writer.writerow({'ProductID': x, 'Name': row[0], 'Category': row[1]})
        x += 1