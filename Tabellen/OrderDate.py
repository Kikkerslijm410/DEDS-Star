import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = '''
SELECT sales_order.id, Day([order_date]) AS [day], Month([order_date]) AS [month], IIf(Month([order_date])<=3,1,IIf(Month([order_date])<=6,2,IIf(Month([order_date])<=9,3,4))) AS quarter, Year([order_date]) AS [year]
FROM sales_order
WHERE (((IsDate([order_date]))<>False));
'''
cursor.execute(query)
results = cursor.fetchall()

# Print
print("=== OrderDateinformatie ===")
x = 0
for row in results:
    x += 1
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

print("Aantal datums:", x)