import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.ticker as mtick

# ----------------------------
# Paths
# ----------------------------
OUTPUT_DIR = Path("outputs")
SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

# ----------------------------
# Global Style (Polished & Modern)
# ----------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",   # Clean & professional (works everywhere)
    "axes.titleweight": "semibold",
    "axes.labelweight": "regular",
    "axes.titlesize": 15,
    "axes.labelsize": 12,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11
})

sns.set_theme(
    style="white",
    rc={
        "axes.edgecolor": "#E0E0E0",
        "axes.linewidth": 0.8,
        "grid.color": "#EFEFEF"
    }
)

# ----------------------------
# Color System 
# ----------------------------
COLORS = {
    "holiday": "#4C6EF5",        # Christmas & New Year
    "non_holiday": "#E6A46A",    # Rest of the year
    "early": "#9CC4E4",
    "late": "#4C6EF5"
}

# ----------------------------
# Formatters
# ----------------------------
def fmt_millions(x, pos):
    return f"${x/1_000_000:.0f}M"

def fmt_billions(x, pos):
    return f"${x/1_000_000_000:.1f}B"

# ============================================================
# 1️⃣ Average Revenue: Christmas vs Rest of Year
# ============================================================
df_baseline = pd.read_csv(OUTPUT_DIR / "03_baseline_comparison.csv")

fig, ax = plt.subplots(figsize=(7.5, 5), constrained_layout=True)

sns.barplot(
    data=df_baseline,
    x="holiday_period",
    y="avg_revenue",
    palette=[COLORS["holiday"], COLORS["non_holiday"]],
    edgecolor="black",
    linewidth=0.6,
    ax=ax
)

ax.set_title(
    "Average Revenue per Movie\nChristmas & New Year vs Rest of the Year",
    pad=14
)
ax.set_xlabel("Release Period", labelpad=8)
ax.set_ylabel("Average Revenue (USD)", labelpad=8)
ax.yaxis.set_major_formatter(mtick.FuncFormatter(fmt_millions))

# Extend y-limit to avoid label clipping
y_max = df_baseline["avg_revenue"].max()
ax.set_ylim(0, y_max * 1.18)

# Value labels
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height()/1_000_000:.1f}M",
        ha="center",
        va="bottom",
        fontsize=11,
        weight="medium",
        clip_on=False
    )

sns.despine()
plt.savefig(SCREENSHOT_DIR / "01_holiday_vs_nonholiday_revenue.png", dpi=220)
plt.close()

# ============================================================
# 2️⃣ Top Genres by Revenue Efficiency
# ============================================================
df_genre = pd.read_csv(OUTPUT_DIR / "05_genre_efficiency.csv")
top_genres = df_genre.sort_values("revenue_per_movie", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(9, 6.5), constrained_layout=True)

sns.barplot(
    data=top_genres,
    y="genres",
    x="revenue_per_movie",
    hue="holiday_period",
    palette={
        "Holiday": COLORS["holiday"],
        "Non-Holiday": COLORS["non_holiday"]
    },
    edgecolor="black",
    linewidth=0.4,
    ax=ax
)

ax.set_title(
    "Top Genres by Revenue per Movie\nChristmas & New Year vs General Releases",
    pad=14
)
ax.set_xlabel("Average Revenue per Movie (USD)", labelpad=8)
ax.set_ylabel("Genre", labelpad=8)
ax.xaxis.set_major_formatter(mtick.FuncFormatter(fmt_millions))

ax.legend(
    title="Release Window",
    labels=["Christmas & New Year", "Rest of the Year"],
    frameon=False,
    loc="lower right"
)

sns.despine()
plt.savefig(SCREENSHOT_DIR / "02_top_genres_revenue_efficiency.png", dpi=220)
plt.close()

# ============================================================
# 3️⃣ Early vs Late Holiday Window
# ============================================================
df_timing = pd.read_csv(OUTPUT_DIR / "06_holiday_release_timing.csv")

fig, ax = plt.subplots(figsize=(7.5, 5), constrained_layout=True)

sns.barplot(
    data=df_timing,
    x="holiday_window",
    y="total_revenue",
    palette=[COLORS["early"], COLORS["late"]],
    edgecolor="black",
    linewidth=0.6,
    ax=ax
)

ax.set_title(
    "Total Revenue During Holiday Season\nEarly vs Late Christmas Window",
    pad=14
)
ax.set_xlabel("Holiday Release Window", labelpad=8)
ax.set_ylabel("Total Revenue (USD)", labelpad=8)
ax.yaxis.set_major_formatter(mtick.FuncFormatter(fmt_billions))

# Extend y-limit
y_max = df_timing["total_revenue"].max()
ax.set_ylim(0, y_max * 1.18)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height()/1_000_000_000:.1f}B",
        ha="center",
        va="bottom",
        fontsize=11,
        weight="medium",
        clip_on=False
    )

sns.despine()
plt.savefig(SCREENSHOT_DIR / "03_holiday_release_timing.png", dpi=220)
plt.close()

print("Visualizations saved to /screenshots")
