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
SELECT sales_order.id, product.quantity, product.unit_price, sales_order.order_date, customer.id, product.id
FROM customer INNER JOIN (product INNER JOIN (sales_order INNER JOIN sales_order_item ON sales_order.id = sales_order_item.id) ON product.id = sales_order_item.prod_id) ON customer.id = sales_order.cust_id;
'''
cursor.execute(query)
results = cursor.fetchall()

# Create a directory to store the data
if not os.path.exists('ETL/Output'):
    os.makedirs('ETL/Output')

with open('ETL/Output/Order.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['ID', 'Quantity', 'Unit_price', 'Order_date', 'Customer', 'Product']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow({'ID': row[0], 'Quantity': row[1], 'Unit_price': row[2], 'Order_date': row[3], 'Customer': row[4], 'Product': row[5]})
