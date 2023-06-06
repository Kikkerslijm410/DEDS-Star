import supabase
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Initialize Supabase client
supabase_url = 'https://dukkznhovjjzfslnleyy.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR1a2t6bmhvdmpqemZzbG5sZXl5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NDMxMzI5NywiZXhwIjoxOTk5ODg5Mjk3fQ.2BBtSMjiJzyZNumptBJ-apSKI3H5DM3RdCQ8Z1z3ku8'
client = supabase.create_client(supabase_url, supabase_key)

# OutdoorFusion Order data
table = client.table("OutdoorFusion.Order")
response = table.select('*').execute().data
df = pd.DataFrame(response)

# Selecteer de relevante variabelen
X = df[['Product']]

# Controleer of er ontbrekende waarden in de gegevens zijn
print(X.isnull().sum())

# Controleer of er outliers in de gegevens zijn
print(X.describe())

# Normaliseer de gegevens
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Bepaal het aantal clusters met de Elbow-methode
inertia = []
for k in range(1, 9):
    kmeans = KMeans(n_clusters=k, n_init='auto', random_state=0)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
plt.plot(range(1, 9), inertia)
plt.xlabel('Aantal clusters')
plt.ylabel('Som van afstanden tot de dichtstbijzijnde clustercentra')
plt.title('Elbow-methode')
plt.show()

# K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_

# Evaluatie van de clustering
df['KMEANS_CLUSTER'] = labels
print(df.groupby(['ShippingDestination', 'KMEANS_CLUSTER'])['Product'].count())
