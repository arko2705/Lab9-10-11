import mysql.connector
import pandas as pd

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='arko5'
)
gender_query = """
SELECT 
    gender,
    COUNT(*) as count
FROM 
    cust_details
WHERE 
    gender IN ('M', 'F')  -- Only count M/F if other values exist
GROUP BY 
    gender
"""

df_gender = pd.read_sql(gender_query, conn)
# Initialize counts
male_count = 0
female_count = 0

# Extract values from query results
for _, row in df_gender.iterrows():
    if row['gender'] == 'M':
        male_count = row['count']
    elif row['gender'] == 'F':
        female_count = row['count']

# Calculate ratio (handle division by zero)
try:
    ratio = male_count / female_count
except ZeroDivisionError:
    ratio = float('inf')  # If no female customers

    report_data = {
    'Metric': ['Total Customers', 'Male Customers', 'Female Customers', 'Male:Female Ratio'],
    'Value': [male_count + female_count, male_count, female_count, f"{ratio:.2f}:1"]
}

df_report = pd.DataFrame(report_data)
df_report.to_csv('gender_ratio_report.csv', index=False)
print("Gender ratio report generated successfully!")

conn.close()