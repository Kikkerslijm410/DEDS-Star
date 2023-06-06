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
SELECT customer.id, customer.company_name, fname, customer.address, customer.city, state.country
FROM state INNER JOIN customer ON state.state_id = customer.state;
'''
cursor.execute(query)
results = cursor.fetchall()

# Create a directory to store the data
if not os.path.exists('ETL/Output'):
    os.makedirs('ETL/Output')

with open('ETL/Output/Customer.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['ID', 'Company_name', 'fname', 'adress', 'city', 'country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow({'ID': row[0], 'Company_name': row[1], 'fname': row[2], 'adress': row[3], 'city': row[4], 'country': row[5]})
        