import pandas as pd
import supabase

# Initialize Supabase client
supabase_url = 'https://dukkznhovjjzfslnleyy.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR1a2t6bmhvdmpqemZzbG5sZXl5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NDMxMzI5NywiZXhwIjoxOTk5ODg5Mjk3fQ.2BBtSMjiJzyZNumptBJ-apSKI3H5DM3RdCQ8Z1z3ku8'

client = supabase.create_client(supabase_url, supabase_key)
# Orders data
table_name = "OutdoorFusion.Order"
table = client.table(table_name)
response = table.select('*').execute()
data = response.data
orders = pd.DataFrame(data)
print (orders)
