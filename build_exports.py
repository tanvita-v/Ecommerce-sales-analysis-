import pandas as pd, numpy as np
from pathlib import Path
DATA_RAW = Path('../data/ecommerce_raw.csv')
DATA_CLEAN = Path('../data/ecommerce_clean.csv')
EXPORTS = Path('../data/exports')
EXPORTS.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_RAW)
for c in ['Order Date','Ship Date']:
    if c in df.columns:
        df[c] = pd.to_datetime(df[c], errors='coerce')
df = df.dropna(subset=['Order Date']).drop_duplicates()
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)
df['Week'] = df['Order Date'].dt.to_period('W').apply(lambda r: r.start_time)
df['Profit Margin'] = np.where(df['Sales']>0, df['Profit']/df['Sales'], np.nan)
df.to_csv(DATA_CLEAN, index=False)
fact = df[['Order ID','Order Date','Customer ID','Product ID','Quantity','Unit Price','Discount','Sales','Profit','Region','Segment','Year','Month','YearMonth','Week']].copy()
fact.to_csv(EXPORTS / 'fact_sales.csv', index=False)
dim_cust = (df.groupby(['Customer ID','Customer Name','Segment'], as_index=False).size().rename(columns={'size':'Orders'}))
dim_cust.to_csv(EXPORTS / 'dim_customers.csv', index=False)
dim_prod = (df.groupby(['Product ID','Product Name','Category','Sub-Category'], as_index=False).size().rename(columns={'size':'Lines'}))
dim_prod.to_csv(EXPORTS / 'dim_products.csv', index=False)
max_date = df['Order Date'].max()
rfm = (df.groupby('Customer ID').agg(Recency=('Order Date', lambda s: (max_date - s.max()).days), Frequency=('Order ID','nunique'), Monetary=('Sales','sum')).reset_index())
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1]).astype(int)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5]).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1,2,3,4,5]).astype(int)
rfm['RFM_Score'] = rfm[['R_Score','F_Score','M_Score']].sum(axis=1)
rfm.to_csv(EXPORTS / 'rfm_scores.csv', index=False)
kpis = {'total_revenue': float(df['Sales'].sum()), 'total_profit': float(df['Profit'].sum()), 'orders': int(df.shape[0]), 'avg_order_value': float(df['Sales'].mean()), 'profit_margin_pct': float((df['Profit'].sum()/df['Sales'].sum())*100.0) if df['Sales'].sum() else 0.0, 'unique_customers': int(df['Customer ID'].nunique()), 'unique_products': int(df['Product ID'].nunique()), 'period_start': str(df['Order Date'].min().date()), 'period_end': str(df['Order Date'].max().date())}
pd.DataFrame([kpis]).to_csv(EXPORTS / 'kpi_summary.csv', index=False)
print('Exports rebuilt in', EXPORTS.resolve())
