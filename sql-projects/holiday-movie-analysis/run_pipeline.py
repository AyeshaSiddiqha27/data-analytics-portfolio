import subprocess
import sys

def run_step(step_name, command):
    print(f"\n Running: {step_name}")
    try:
        subprocess.run([sys.executable] + command, check=True)
        print(f"✅ Completed: {step_name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {step_name}")
        sys.exit(1)

if __name__ == "__main__":
    print("\n Starting Holiday Movie Analysis Pipeline")

    # Step 1: Load raw CSV into SQLite
    run_step(
        "Load raw data into SQLite",
        ["analysis/load_to_sqlite.py"]
    )

    # Step 2: Normalize genres
    run_step(
        "Normalize genres table",
        ["analysis/normalize_genres.py"]
    )

    # Step 3: Run analytical SQL queries
    run_step(
        "Run SQL analysis",
        ["analysis/run_analysis.py"]
    )

    # Step 4: Generate visualizations
    run_step(
        "Generate charts",
        ["analysis/visualize_results.py"]
    )

    print("\n Pipeline completed successfully!")
