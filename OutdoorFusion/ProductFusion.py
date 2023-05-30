import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = '''
SELECT Category, [id] + [name] AS Product
FROM product;
'''

cursor.execute(query)
results = cursor.fetchall()

# Print	(meer als check)
print("=== Productinformatie ===")
x = 0
for row in results:
    x += 1
    product_category = row.Category
    product_product = row.Product
    print("Product Category:", product_category)
    print("Product:", product_product)
    print("--------------------")
print("Totaal aantal producten:", x)