# Power BI – One‑Click Build

1) Open **Power BI Desktop**.
2) **File → Options and Settings → Options → Global → Security**: ensure external connections are allowed.
3) **Get Data → Text/CSV**, import all files from `../data/exports/`:
   - `fact_sales.csv`
   - `dim_customers.csv`
   - `dim_products.csv`
   - `rfm_scores.csv`
   - `kpi_summary.csv`
4) Create a new table using **Modeling → New Table** and paste the DAX from `Date_Table_DAX.pbitxt`.
5) Create measures using **Modeling → New Measure** and paste from `DAX_Measures.pbitxt`.
6) Set **Model relationships** as described in `Model_Spec.json` (or let Auto detect, then verify).
7) (Optional) Apply theme via **View → Themes → Browse** and select `Theme.json`.
8) Build visuals:
   - Cards: `Total Revenue`, `Total Profit`, `Orders`, `AOV`, `Profit Margin %`
   - Line: `Date[YearMonth]` vs `[Total Revenue]`
   - Bar: Sales by `Category`, `Sub-Category`, `Segment`
   - Scatter: `Discount` vs `Profit` with `Sales` as Size
   - Table/Matrix: `RFM_Score`, `Frequency`, `Monetary`
9) Save as `powerbi/Ecommerce_Customer_Analysis.pbix`.
