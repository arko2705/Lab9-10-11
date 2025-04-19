import pandas as pd
import matplotlib.pyplot as plt
import random
# Mock data
data = {
    "CustomerID": range(1, 101),
    "CustomerAddressType": random.choices(["Home", "Office", "Shipping", "Billing"], k=100)
}

df = pd.DataFrame(data)
df.to_csv("customers_address.csv", index=False)

# Load the dataset
df = pd.read_csv('customers_address.csv') 
print(df.head())  # Check the first 5 rows

# Count address types
address_counts = df['CustomerAddressType'].value_counts()

# Plot
plt.figure(figsize=(10, 6))
address_counts.plot(kind='bar', color='skyblue')
plt.title('Most Common Customer Address Types')
plt.xlabel('Address Type')
plt.ylabel('Count')
plt.savefig('address_types_bar.png')
plt.show()