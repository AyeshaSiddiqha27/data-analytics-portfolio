import sqlite3
import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
DB_PATH = Path("data/movies.db")
SQL_DIR = Path("analysis/sql")
OUTPUT_DIR = Path("outputs")

OUTPUT_DIR.mkdir(exist_ok=True)

# ----------------------------
# Helper function
# ----------------------------
def run_query(sql_filename, output_name=None, preview_rows=5):
    """
    Executes a SQL file against SQLite DB.
    - Uses executescript for DDL (CREATE/DROP/INSERT)
    - Uses read_sql_query for SELECT queries
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    sql_path = SQL_DIR / sql_filename
    query = sql_path.read_text().strip()

    # Detect DDL / non-SELECT scripts
    if not query.lower().startswith("select"):
        cursor.executescript(query)
        conn.commit()
        print(f"🛠️ Executed DDL: {sql_filename}")
        conn.close()
        return

    # SELECT queries
    df = pd.read_sql_query(query, conn)

    if output_name:
        output_path = OUTPUT_DIR / output_name
        df.to_csv(output_path, index=False)
        print(f"✅ Saved: {output_path}")

    print(f"\n--- Preview: {sql_filename} ---")
    print(df.head(preview_rows))

    conn.close()


# ----------------------------
# Main execution flow
# ----------------------------
if __name__ == "__main__":
    # Base view (must run first)
    run_query("00_create_base_view.sql")

    # Task 1: Data quality
    run_query("01_data_quality.sql")

    # Task 2: Baseline comparison
    run_query(
        "03_baseline_comparison.sql",
        "03_baseline_comparison.csv"
    )

    # Task 3: Genre holiday impact
    run_query(
        "04_genre_expansion.sql",
        "04_genre_holiday_analysis.csv"
    )

    # Task 4: Genre efficiency
    run_query(
        "05_genre_efficiency.sql",
        "05_genre_efficiency.csv"
    )

    # Task 5: Holiday timing
    run_query(
        "06_holiday_release_timing.sql",
        "06_holiday_release_timing.csv"
    )
