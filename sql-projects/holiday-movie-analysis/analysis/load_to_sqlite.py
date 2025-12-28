import sqlite3
import pandas as pd

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("movies.db")

# Load raw CSV
df = pd.read_csv("data/raw_movies.csv")

# Rename columns to simpler names (senior hygiene)
df = df.rename(columns={
    "vote_average": "rating"
})

# Select only columns we need for analysis
df = df[[
    "title",
    "release_date",
    "genres",
    "rating",
    "revenue"
]]

# Basic type handling
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Write to SQLite
df.to_sql("movies", conn, if_exists="replace", index=False)

conn.close()

print("SQLite table 'movies' created successfully.")
