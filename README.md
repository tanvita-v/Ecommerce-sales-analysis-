E-commerce Customer Analysis (Python → Power BI)
📌 Project Overview

An end-to-end data analytics project processing one year of e-commerce sales (30K+ transactions) from raw CSVs to actionable business insights.
Data is cleaned, transformed, and enriched in Python, exported as model-ready CSVs, and visualized in Power BI to support executive decision-making.

🚀 Key Highlights

Built a fully automated Python pipeline (build_exports.py) to merge & clean 12 months of sales data.

Generated fact & dimension tables, KPI metrics, RFM scores for customer segmentation.

Developed interactive Power BI dashboards tracking revenue, margins, orders, and customer retention.

RFM & Pareto analysis revealed top 20% of customers generate ~68% of total revenue.

Seasonal trends confirmed November & December as peak months → guided marketing & stock planning.

Identified Electronics & Clothing as highest-margin categories; repeat buyers spend ~1.8× more vs new customers.

Delivered visual storytelling for business stakeholders with clear, data-driven insights.

📁 Repository Structure
ecom_customer_analysis_powerbi/
├── data/
│   ├── ecommerce_raw.csv          # Full merged dataset (local only; not in repo)
│   ├── ecommerce_clean.csv        # Cleaned dataset (local only; not in repo)
│   ├── exports/                   # Sample outputs (full rebuild locally)
│   │   ├── fact_sales.csv
│   │   ├── dim_customers.csv
│   │   ├── dim_products.csv
│   │   ├── rfm_scores.csv
│   │   └── kpi_summary.csv
│   └── README_DATA.md
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_customer_segmentation.ipynb
│   └── 04_kpi_metrics.ipynb
├── powerbi/
│   ├── README_powerbi_instructions.md
│   ├── Date_Table_DAX.pbitxt
│   ├── DAX_Measures.pbitxt
│   ├── Model_Spec.json
│   ├── Theme.json
│   └── Quickstart.md
├── reports/
│   ├── screenshots/
│   └── ecommerce_full_report.pdf
├── visuals/                       # PNG charts from Python analysis
├── scripts/
│   └── build_exports.py
├── requirements.txt
└── README.md

⚙️ How to Run

Clone repo & install dependencies:

pip install -r requirements.txt


Add your dataset:

Place full merged data in data/ecommerce_raw.csv
(or monthly splits in data/splits/ and merge first)

Rebuild exports:

python scripts/build_exports.py


View outputs in data/exports/:

fact_sales.csv → transactions table

dim_customers.csv / dim_products.csv → lookup tables

rfm_scores.csv → customer segmentation

kpi_summary.csv → business KPIs

📊 Power BI Dashboard
Steps

Open Power BI Desktop

Get Data → Text/CSV → import all data/exports/*.csv

Create Date table from Date_Table_DAX.pbitxt

Add measures from DAX_Measures.pbitxt

Set model relationships per Model_Spec.json

Apply theme Theme.json

Build visuals:

KPI Cards → Total Revenue, Total Profit, Orders, AOV, Profit Margin %

Monthly/Weekly trend → Revenue & Profit

Sales by Category / Sub-Category / Segment

Discount vs Profit scatter

RFM heatmap / segment distribution

📈 Example Insights

Top 20% customers → ~68% of total revenue.

Peak months → November & December (holiday demand surge).

Highest margins → Electronics & Clothing.

Customer loyalty → Repeat buyers spend ~1.8× more vs new customers.
