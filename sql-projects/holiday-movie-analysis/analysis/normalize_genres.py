import pandas as pd
import ast
import sqlite3

# Load movies table
conn = sqlite3.connect("data/movies.db")
movies = pd.read_sql("SELECT * FROM movies", conn)

rows = []

for _, row in movies.iterrows():
    if pd.isna(row["genres"]):
        continue

    try:
        genres = ast.literal_eval(row["genres"])
        for g in genres:
            rows.append({
                "id": row["id"],
                "title": row["title"],
                "genres": g["name"],
                "rating": row["rating"],
                "revenue": row["revenue"],
                "release_date": row["release_date"]
            })
    except Exception:
        continue

genre_df = pd.DataFrame(rows)

# Save normalized table
genre_df.to_sql("movie_genres", conn, if_exists="replace", index=False)

conn.close()

print("✅ movie_genres table created")
