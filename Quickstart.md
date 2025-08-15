# Power BI Quickstart

1. Open **Power BI Desktop** → **Get Data → Text/CSV** and import all CSVs in `data/exports/`.
2. Go to **Modeling → New Table**, paste contents of `Date_Table_DAX.pbitxt`.
3. Go to **Modeling → New Measure**, paste contents of `DAX_Measures.pbitxt`.
4. Open **Model view**:
   - Link `fact_sales[Customer ID]` → `dim_customers[Customer ID]` (Many-to-one, single)
   - Link `fact_sales[Product ID]` → `dim_products[Product ID]` (Many-to-one, single)
   - Link `Date[Date]` → `fact_sales[Order Date]` (One-to-many, single). Ensure this one is **Active**.
5. (Optional) **View → Themes → Browse** and select `Theme.json`.
6. Build visuals:
   - Cards: `[Total Revenue]`, `[Total Profit]`, `[Orders]`, `[AOV]`, `[Profit Margin %]`
   - Line: `Date[YearMonth]` vs `[Total Revenue]` (add `[Revenue LY]` for YoY)
   - Bar: `Category` / `Sub-Category` / `Segment` vs `[Total Revenue]`
   - Scatter: `Discount` (X) vs `Profit` (Y), `Sales` as Size, `Category` as Legend
   - Matrix: `RFM_Score`, `Frequency`, `Monetary`
7. Save as `powerbi/Ecommerce_Customer_Analysis.pbix`.
