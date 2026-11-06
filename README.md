# E-Commerce Sales & Customer Transaction Analytics

An exploratory data analytics project examining customer purchasing behavior, revenue trends, payment channel efficiency, and RFM (Recency, Frequency, Monetary) segmentation across 1,500+ order records.

##  Project Overview
- **RFM Segmentation:** Segmented customer base to analyze customer retention and spend distribution.
- **Revenue & Channel Analysis:** Analyzed sales velocity across product categories and quantified return/cancellation rates across payment modes.
- **SQL Analytics Pipeline:** Designed multi-level aggregations and window functions (`DENSE_RANK`) to identify high-value customer cohorts.

##  Tech Stack
- **Languages:** Python (Pandas, NumPy, Matplotlib, Seaborn)
- **Database / Querying:** SQL (MySQL compatible)
- **Techniques:** Exploratory Data Analysis (EDA), RFM Cohort Analysis, Business KPI Reporting

##  Sample Outputs
- `visualizations/category_revenue.png`
- `visualizations/rfm_spend_distribution.png`

##  Execution
```bash
python scripts/sales_analysis.py