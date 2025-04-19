import mysql.connector
import pandas as pd

# Connect to database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='arko5'
)

# Define parameters
target_language = 'English'
min_age = 20
max_age = 30

# SQL query with parameters
query = f"""
SELECT 
    CST_ID,
    age,
    language_spoken
FROM 
    cust_details
WHERE 
    language_spoken = '{target_language}'
    AND age BETWEEN {min_age} AND {max_age}
"""

# Execute query and load into DataFrame
df_customers = pd.read_sql(query, conn)

# Save to CSV
df_customers.to_csv('filtered_customers.csv', index=False)
print(f"Found {len(df_customers)} customers matching criteria")

conn.close()
print("Connection to databse closed")