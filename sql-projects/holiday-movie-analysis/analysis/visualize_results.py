import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
OUTPUT_DIR = Path("outputs")
SCREENSHOT_DIR = Path("screenshots")

SCREENSHOT_DIR.mkdir(exist_ok=True)

sns.set(style="whitegrid")

# ----------------------------
# 1️⃣ Holiday vs Non-Holiday Revenue
# ----------------------------
df_baseline = pd.read_csv(OUTPUT_DIR / "03_baseline_comparison.csv")

plt.figure(figsize=(6, 4))
sns.barplot(
    data=df_baseline,
    x="holiday_period",
    y="avg_revenue",
    palette="muted"
)

plt.title("Average Revenue: Holiday vs Non-Holiday Releases")
plt.ylabel("Average Revenue (USD)")
plt.xlabel("Release Period")

plt.tight_layout()
plt.savefig(SCREENSHOT_DIR / "holiday_vs_nonholiday_revenue.png")
plt.close()

# ----------------------------
# 2️⃣ Top Genres by Revenue Efficiency
# ----------------------------
df_genre_eff = pd.read_csv(OUTPUT_DIR / "05_genre_efficiency.csv")

top_genres = (
    df_genre_eff
    .sort_values("revenue_per_movie", ascending=False)
    .head(10)
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=top_genres,
    y="genres",
    x="revenue_per_movie",
    hue="holiday_period"
)

plt.title("Top Genres by Revenue per Movie")
plt.xlabel("Average Revenue per Movie (USD)")
plt.ylabel("Genre")

plt.tight_layout()
plt.savefig(SCREENSHOT_DIR / "top_genres_revenue_efficiency.png")
plt.close()

# ----------------------------
# 3️⃣ Early vs Late Holiday Releases
# ----------------------------
df_timing = pd.read_csv(OUTPUT_DIR / "06_holiday_release_timing.csv")

plt.figure(figsize=(6, 4))
sns.barplot(
    data=df_timing,
    x="holiday_window",
    y="total_revenue",
    palette="deep"
)

plt.title("Total Revenue: Early vs Late Holiday Releases")
plt.ylabel("Total Revenue (USD)")
plt.xlabel("Holiday Window")

plt.tight_layout()
plt.savefig(SCREENSHOT_DIR / "holiday_release_timing.png")
plt.close()

print("All visualizations saved to /screenshots")
