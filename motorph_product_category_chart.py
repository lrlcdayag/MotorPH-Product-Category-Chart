from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

DATA_FILE = Path(
    r"C:\python\MotorPH_Data_Preprocessing\MotorPH_Products_Cleaned_2025.csv"
)
OUTPUT_FILE = DATA_FILE.with_name("MotorPH_Product_Category_Distribution.png")

if not DATA_FILE.is_file():
    raise FileNotFoundError(f"Cleaned product file not found: {DATA_FILE}")

products = pd.read_csv(DATA_FILE)

required_columns = {"Product Name", "Product Type"}
missing_columns = required_columns - set(products.columns)
if missing_columns:
    raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

if products.empty or products[list(required_columns)].isna().any().any():
    raise ValueError("The product dataset is empty or has missing names/categories.")

if products["Product Name"].duplicated().any():
    raise ValueError("Duplicate product names found; review the catalog before plotting.")

category_counts = products["Product Type"].value_counts().sort_values()

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(10, max(6, len(category_counts) * 0.38)))

bars = ax.barh(category_counts.index, category_counts.values, color="#238A8D")

ax.set_title("MotorPH Products by Category", fontsize=16, weight="bold", pad=14)
ax.set_xlabel("Number of products")
ax.set_ylabel("")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(axis="x", linestyle="--", alpha=0.45)
ax.grid(axis="y", visible=False)

ax.set_xlim(0, category_counts.max() * 1.18)
ax.bar_label(bars, padding=4, fontsize=9)

fig.tight_layout()
fig.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
plt.show()

print(f"Chart saved to: {OUTPUT_FILE}")
print("\nProduct counts by category:")
print(category_counts.sort_values(ascending=False))