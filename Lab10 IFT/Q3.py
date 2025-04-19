import mysql.connector
import pandas as pd

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='arko5'
)
query = """
SELECT 
    country,
    language_spoken,
    COUNT(*) AS speaker_count
FROM 
    cust_details
GROUP BY 
    country, language_spoken
ORDER BY 
    country, speaker_count DESC
"""
df_lang_dist = pd.read_sql(query, conn)
pivot_table = df_lang_dist.pivot(
    index='country',
    columns='language_spoken',
    values='speaker_count'
).fillna(0)  # Replace NaN with 0
pivot_table['Total'] = pivot_table.sum(axis=1)
# Save raw distribution data
df_lang_dist.to_csv('language_distribution_raw.csv', index=False)

# Save pivot table (more readable)
pivot_table.to_csv('language_distribution_pivot.csv')

print("Language distribution reports saved successfully!")
conn.close()