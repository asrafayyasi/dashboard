import pandas as pd
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
import altair as alt
import matplotlib.pyplot as plt

orders_df = pd.read_csv("orders_df_clean.csv")
orders_df.head()

st.header('Data Order Perusahaan :sparkles:')

# Konversi kolom order_purchase_timestamp ke datetime
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

# Ekstrak bulan dan tahun
orders_df['purchase_month'] = orders_df['order_purchase_timestamp'].dt.month
orders_df['purchase_year'] = orders_df['order_purchase_timestamp'].dt.year

# Group by bulan dan tahun dan hitung jumlah pembelian
trend_data = orders_df.groupby(['purchase_year', 'purchase_month']).size().reset_index(name='purchase_count')

# Plotting the trend
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(trend_data['purchase_count'], marker='o')
ax.set_title('Trend Pembelian dari Waktu ke Waktu')
ax.set_xlabel('Bulan dan Tahun')
ax.set_ylabel('Jumlah Pembelian')
ax.set_xticks(range(len(trend_data)))
ax.set_xticklabels([f"{y}-{m}" for y, m in zip(trend_data['purchase_year'], trend_data['purchase_month'])], rotation=45)

# Tampilkan plot di Streamlit
st.pyplot(fig)


# Assuming df is your DataFrame
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
orders_df['order_delivered_customer_date'] = pd.to_datetime(orders_df['order_delivered_customer_date'])
orders_df['purchase_year'] = orders_df['order_purchase_timestamp'].dt.year
orders_df['purchase_month'] = orders_df['order_purchase_timestamp'].dt.month
orders_df['delivery_duration'] = (orders_df['order_delivered_customer_date'] - orders_df['order_purchase_timestamp']).dt.days

# Group by bulan dan tahun dan hitung rata-rata durasi pengiriman
trend_pengiriman = orders_df.groupby(['purchase_year', 'purchase_month'])['delivery_duration'].mean().reset_index(name='average_delivery_duration')

# Plotting the trend
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(trend_pengiriman['purchase_year'].astype(str) + '-' + trend_pengiriman['purchase_month'].astype(str), trend_pengiriman['average_delivery_duration'], marker='o')
ax.set_title('Trend Durasi Pengiriman Bulan ke Bulan')
ax.set_xlabel('Bulan dan Tahun')
ax.set_ylabel('Rata-rata Durasi Pengiriman (Hari)')
ax.set_xticks(range(len(trend_pengiriman)))
ax.set_xticklabels([f"{y}-{m}" for y, m in zip(trend_pengiriman['purchase_year'], trend_pengiriman['purchase_month'])], rotation=45)

# Tampilkan plot di Streamlit
st.pyplot(fig)