import mysql.connector
import pandas as pd

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='arko5',
)
print("Connected to MySQL database successfully!")
# Write your SQL query to select all data from the student table
query = "SELECT * FROM cust_details"

# Use pandas to read the SQL query results into a DataFrame
df = pd.read_sql(query, conn)

# Let's verify we got some data
print("Successfully fetched data!")
print(f"Number of records: {len(df)}")
print("First few rows:")
print(df.head())

# (We'll close the connection in the next step)
# STEP 4: Save DataFrame to CSV
csv_filename = "CustomerDetails.csv"
df.to_csv(csv_filename, index=False)  # index=False avoids extra column numbers

print(f"\nSUCCESS: Saved {len(df)} records to '{csv_filename}'!")
# Close the connection (IMPORTANT to avoid resource leaks)
conn.close()
print("Database connection closed.")