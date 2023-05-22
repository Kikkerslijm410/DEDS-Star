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

for row in results:
    product_id = row.id
    product_name = row.name
    product_description = row.description
    product_category = row.Category

    print("Product ID:", product_id)
    print("Product Name:", product_name)
    print("Product Description:", product_description)
    print("Product Category:", product_category)
    print("--------------------")
