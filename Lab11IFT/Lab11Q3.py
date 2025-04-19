import pandas as pd
import matplotlib.pyplot as plt
import random


# Mock data
data = {
    "CustomerID": range(1, 101),
    "CustomerPreferredLanguage": random.choices(["English", "Spanish", "French", "German"], k=100)
}

df = pd.DataFrame(data)
df.to_csv("customers_language.csv", index=False)

# Load the dataset
df = pd.read_csv('customers_language.csv')  
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