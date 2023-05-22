import pyodbc

# Verbinding maken met de Access-database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)

# Een cursor maken om de queries uit te voeren
cursor = conn.cursor()

# Query 1: Klanteninformatie ophalen
query_customer = '''
SELECT customer.id, customer.company_name, fname, customer.address, customer.city, state.country
FROM state INNER JOIN customer ON state.state_id = customer.state;
'''
cursor.execute(query_customer)
results_customer = cursor.fetchall()

# Query 2: Productinformatie ophalen
query_product = '''
SELECT product.id, product.name, product.description, product.Category
FROM product;
'''
cursor.execute(query_product)
results_product = cursor.fetchall()

# Query 3: Datuminformatie ophalen
query_date = '''
SELECT sales_order.id, Day([order_date]) AS [day], Month([order_date]) AS [month], IIf(Month([order_date])<=3,1,IIf(Month([order_date])<=6,2,IIf(Month([order_date])<=9,3,4))) AS quarter, Year([order_date]) AS [year]
FROM sales_order
WHERE (((IsDate([order_date]))<>False));
'''
cursor.execute(query_date)
results_date = cursor.fetchall()

print("=== Klanteninformatie ===")
for row in results_customer:
    customer_id = row.id
    company_name = row.company_name
    fname = row.fname
    address = row.address
    city = row.city
    country = row.country

    print("Customer ID:", customer_id)
    print("Company Name:", company_name)
    print("Name:", fname)
    print("Address:", address)
    print("City:", city)
    print("Country:", country)
    print("--------------------")

print("=== Productinformatie ===")
for row in results_product:
    product_id = row.id
    product_name = row.name
    product_description = row.description
    product_category = row.Category

    print("Product ID:", product_id)
    print("Product Name:", product_name)
    print("Product Description:", product_description)
    print("Product Category:", product_category)
    print("--------------------")

print("=== Verkooporderinformatie ===")
for row in results_date:
    sales_order_id = row.id
    day = row.day
    month = row.month
    quarter = row.quarter
    year = row.year

    print("Sales Order ID:", sales_order_id)
    print("Day:", day)
    print("Month:", month)
    print("Quarter:", quarter)
    print("Year:", year)
    print("--------------------")