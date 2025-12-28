import sqlite3
import pandas as pd

conn = sqlite3.connect("data/movies.db")

# 1. List all tables
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables in database:")
print(tables)

# 2. Show 5 rows from each table
for table in tables["name"]:
    print(f"\n--- {table} (first 5 rows) ---")
    df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 5;", conn)
    print(df)

conn.close()
