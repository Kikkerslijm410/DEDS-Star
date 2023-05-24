import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = '''
SELECT sales_order.id, product.quantity, product.unit_price, sales_order.order_date, customer.fname, product.name
FROM customer INNER JOIN (product INNER JOIN (sales_order INNER JOIN sales_order_item ON sales_order.id = sales_order_item.id) ON product.id = sales_order_item.prod_id) ON customer.id = sales_order.cust_id;
'''
cursor.execute(query)
results = cursor.fetchall()

# Print
print("=== Orderinformatie ===")
x = 0
for row in results:
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

print("Aantal orders:", x)