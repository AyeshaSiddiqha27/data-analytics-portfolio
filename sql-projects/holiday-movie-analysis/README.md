# 🎬 Holiday Movie Performance Analysis (SQL + Python)

This project analyzes how **movie release timing during the holiday season** impacts **revenue and audience ratings**, using a reproducible SQL + Python analytics pipeline. The objective is to simulate **real-world data analyst work**, from raw data ingestion to business insights and visual storytelling.

The analysis focuses on understanding whether holiday releases outperform non-holiday releases, which genres benefit most from holiday timing, and whether releasing closer to Christmas and New Year generates higher revenue than early December releases.

---

## Business Context & Questions

Studios frequently target the holiday season for major releases, expecting higher audience turnout. However, holiday releases are fewer in number compared to non-holiday releases, and competition is intense. This project answers the following business questions:

- Do holiday releases generate higher revenue despite lower volume?
- Are audience ratings significantly different between holiday and non-holiday movies?
- Which genres perform best during holiday periods?
- Is it more profitable to release movies early in December or closer to Christmas and New Year?

---

## Dataset

The dataset contains movie metadata including:
- Id
- Movie title
- Release date
- Genres
- Average rating
- Revenue

The raw dataset is stored as a CSV file and loaded into a SQLite database for analysis. Genres are normalized into a separate table to enable accurate genre-level analysis.

---

## Tech Stack

- SQL (SQLite)
- Python (pandas, sqlite3)
- Seaborn & Matplotlib for visualization
- VS Code for development
- GitHub for version control

---

## Project Structure

holiday-movie-analysis/
│
├── run_pipeline.py                # Single entry-point to run everything
│
├── analysis/
│   ├── load_to_sqlite.py           # Load raw CSV into SQLite
│   ├── normalize_genres.py         # Normalize genres (1 movie → many genres)
│   ├── run_analysis.py             # Execute SQL analysis & export results
│   ├── visualize_results.py        # Generate charts using Seaborn
│   └── sql/
│       ├── 00_create_base_view.sql
│       ├── 01_data_quality.sql
│       ├── 03_baseline_comparison.sql
│       ├── 04_genre_holiday_analysis.sql
│       ├── 05_genre_efficiency.sql
│       └── 06_holiday_release_timing.sql
│
├── data/
│   ├── raw_movies.csv              # Original dataset
│   └── movies.db                   # SQLite database
│
├── outputs/                        # CSV outputs from SQL analysis
├── screenshots/                    # Saved charts for insights
└── README.md


---

## Execution Guide (One Command)

The entire pipeline is designed to be reproducible with **a single command**.

From the project root, run:

```bash
python run_pipeline.py

## What the Pipeline Does

The pipeline loads the raw CSV file into a SQLite database (movies table), then normalizes the genres so that each movie–genre combination is stored as a separate row in the movie_genres table. A reusable SQL view (base_holiday_movies) is created to classify movies into Holiday and Non-Holiday periods based on their release dates. Analytical SQL queries are then executed to generate insights, with results exported as CSV files. Finally, visualizations are generated from these outputs and saved as image files for storytelling and presentation.

## Analysis & Key Insights

Holiday releases generate comparable total revenue despite significantly fewer movies, indicating stronger audience concentration during the holiday season. Average ratings between holiday and non-holiday releases are very similar, suggesting that revenue differences are driven more by audience availability than perceived content quality. Certain genres consistently generate higher revenue per movie during holiday periods. Movies released closer to Christmas and New Year outperform early December releases in total revenue, highlighting the importance of precise release timing.

## Data Quality Considerations

Missing release dates and zero-revenue records are explicitly measured and documented. Revenue distributions are highly skewed, so median-aware thinking is applied during interpretation. Genre normalization is handled in Python to avoid unreliable JSON parsing in SQL.

## Visual Outputs

The project includes executive-ready visualizations such as Holiday vs Non-Holiday average revenue comparison, Top genres by revenue per movie, and Early vs Late holiday release performance. All charts are saved in the screenshots/ folder and can be reused for presentations, blogs, or LinkedIn posts.

## Why This Project Matters

This project demonstrates end-to-end analytics pipeline design, clean SQL with reusable views, Python-driven orchestration, business-focused interpretation of imperfect data, and the level of reproducibility and clarity expected at a Senior Data Analyst level. It goes beyond writing queries and focuses on how insights are generated, validated, and communicated.

## Author

Ayesha Siddiqha  
Data Analyst | SQL & Python
Germany  
[LinkedIn](https://www.linkedin.com/in/ayesha-siddiqha-)  

