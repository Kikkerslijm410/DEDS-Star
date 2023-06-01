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
SELECT product.id, product.name, product.description, product.Category
FROM product;
'''
cursor.execute(query)
results = cursor.fetchall()

# Create a directory to store the data
if not os.path.exists('Output'):
    os.makedirs('Output')

with open('Output/Product.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['ID', 'Name', 'Description', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow({'ID': row[0], 'Name': row[1], 'Description': row[2], 'Category': row[3]})