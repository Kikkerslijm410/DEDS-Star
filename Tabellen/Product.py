import pyodbc

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

# Print	
print("=== Productinformatie ===")
x = 0
for row in results:
    x += 1
    product_id = row.id
    product_name = row.name
    product_description = row.description
    product_category = row.Category

    print("Product ID:", product_id)
    print("Product Name:", product_name)
    print("Product Description:", product_description)
    print("Product Category:", product_category)
    print("--------------------")

print("Aantal producten:", x)