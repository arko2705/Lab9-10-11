import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Mock data
data = {
     "CustomerID": range(1, 101),
    "EndDate": [datetime.now() + timedelta(days=random.randint(-365, 365)) if random.random() > 0.5 else None for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv("customers_status.csv", index=False)

# Load the dataset
df = pd.read_csv('customers_status.csv') 
print(df.head())  # Check the first 5 rows

# Count languages
language_counts = df['CustomerPreferredLanguage'].value_counts()

# Plot
plt.figure(figsize=(10, 6))
language_counts.plot(kind='barh', color='orange')  # 'barh' for horizontal bars
plt.title('Customer Language Preferences')
plt.xlabel('Count')
plt.ylabel('Language')
plt.savefig('language_preferences.png')
plt.show()