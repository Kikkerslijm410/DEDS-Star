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

# Query 4: Orderinformatie samenstellen
query = '''
SELECT sales_order.id, product.quantity, product.unit_price, sales_order.order_date, customer.fname, product.name
FROM customer INNER JOIN (product INNER JOIN (sales_order INNER JOIN sales_order_item ON sales_order.id = sales_order_item.id) ON product.id = sales_order_item.prod_id) ON customer.id = sales_order.cust_id;
'''
cursor.execute(query)
Order_results = cursor.fetchall()

print("=== Orderinformatie ===")
x = 0
for row in Order_results:
    x += 1
    sales_order_id = row.id
    quantity = row.quantity
    unit_price = row.unit_price
    order_date = row.order_date
    customer_name = row.fname
    product_name = row.name

    print("Sales Order ID:", sales_order_id)
    print("Quantity:", quantity)
    print("Unit Price:", unit_price)
    print("Order Date:", order_date)
    print("Customer Name:", customer_name)
    print("Product Name:", product_name)
    print("--------------------")
    
print ("Totaal aantal orders:", x)