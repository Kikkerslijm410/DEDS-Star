import pyodbc

# Connect to database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Database/AenC.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Set the query
query = '''
SELECT customer.id, customer.company_name, fname, customer.address, customer.city, state.country
FROM state INNER JOIN customer ON state.state_id = customer.state;
'''
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print 
for row in results:
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