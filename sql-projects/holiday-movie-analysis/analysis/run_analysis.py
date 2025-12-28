import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/movies.db"
SQL_DIR = Path("analysis/sql")
OUTPUT_DIR = Path("outputs")

# Ensure outputs folder exists
OUTPUT_DIR.mkdir(exist_ok=True)

def run_query(sql_filename, output_name=None, preview_rows=5):
    conn = sqlite3.connect(DB_PATH)

    sql_path = SQL_DIR / sql_filename
    query = sql_path.read_text()

    df = pd.read_sql_query(query, conn)

    if output_name:
        output_path = OUTPUT_DIR / output_name
        df.to_csv(output_path, index=False)
        print(f"Saved output → {output_path}")

    print(f"\n--- Preview: {sql_filename} ---")
    print(df.head(preview_rows))

    conn.close()

if __name__ == "__main__":
    # Task 1: Data quality assessment
    run_query("01_data_quality.sql")

    # Task 2: Holiday classification logic
    
    run_query("02_holiday_flag.sql")

    # Task 3: Baseline performance comparison
    run_query("03_baseline_comparison.sql", "03_baseline_comparison.csv")

    # Task 4: Genre-level holiday impact
    run_query("04_genre_expansion.sql", "04_genre_holiday_analysis.csv")

    run_query("05_genre_efficiency.sql", "05_genre_efficiency.csv")



