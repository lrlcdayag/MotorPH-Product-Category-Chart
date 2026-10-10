# Repository includes:
MotorPH_Product_Category_Distribution.png: High-resolution horizontal bar chart visualizing the distribution of MotorPH products across all 17 motorcycle categories, highlighting market concentration in scooters and core commuter models.

MotorPH_Products_Cleaned_2025.csv: Standardized product catalog containing all 50 SKUs with parsed product types, corrected titles, formatted unit prices, and validated manufacturing and acquisition years.

# Product Category Chart (python script)
(motorph_product_category_chart.py) Python script utilizing matplotlib and pandas to generate, format, and save the product category distribution chart directly from the cleaned catalog dataset.

# Reasoning for chart type selected 
A bar chart is ideal for displaying categorical distributions with numerous labels. It ranks categories vertically, providing long text labels with optimal legibility without tilting or overlapping.

Categories are sorted in ascending order so the highest-volume categories appear at the top. Direct data labels display exact SKU counts alongside each bar to eliminate visual guessing.

# Key insights derived from the visualization
Scooter Market Leadership: Scooters form MotorPH’s largest category at 12 models (24% of total catalog SKUs), aligning inventory with high-turnover urban commuter demand.   

Core Category Concentration: The top 5 categories—Scooter (12), Naked bike (7), Sport (4), Cruiser (4), and Adventure (4)—make up 62% (31 SKUs) of the product portfolio.   

High Niche Fragmentation: 7 out of 17 categories contain only a single model (41% single-SKU categories), driving up warehousing overhead and highlighting opportunities for catalog rationalization
