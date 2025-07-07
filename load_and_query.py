import pandas as pd
import sqlite3

# Load Excel
df = pd.read_excel("ecommerce_dataset.xlsx")
print("Excel loaded ✅")

# check column types for debugging
print(df.dtypes)

# convert user_ID and product_ID from object types to strings to avoid OverflowError
df['User_ID'] = df['User_ID'].astype(str)
df['Product_ID'] = df['Product_ID'].astype(str)

# Create database
conn = sqlite3.connect("ecommerce.db")
df.to_sql("transactions", conn, if_exists="replace", index=False)
print("Data inserted into SQLite ✅")

# Run sample query
query = """
SELECT * from transactions LIMIT 10
"""

result = pd.read_sql_query(query, conn)
print("\nQuery Result:")
print(result)

conn.close()