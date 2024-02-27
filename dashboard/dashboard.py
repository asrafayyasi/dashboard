import pandas as pd
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
import altair as alt

orders_df = pd.read_csv("orders_df_clean.csv")
orders_df.head()

st.header('Data Order Perusahaan :sparkles:')


df = pd.DataFrame({
    'order_purchase_timestamp': orders_df['order_purchase_timestamp'],
    'order_delivered_customer_date': orders_df['order_delivered_customer_date'],
    'delivery_duration': orders_df['delivery_duration']
})

# Konversi ke format waktu
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])

# Ekstrak informasi bulan dan tahun
df['purchase_month'] = df['order_purchase_timestamp'].dt.month
df['purchase_year'] = df['order_purchase_timestamp'].dt.year

# Hitung rata-rata durasi pengiriman
trend_data = df.groupby(['purchase_year', 'purchase_month'])['delivery_duration'].mean().reset_index(name='average_delivery_duration')

# Tampilkan plot dengan Altair
chart = alt.Chart(trend_data).mark_line().encode(
    x='purchase_year:T',
    y='average_delivery_duration:Q'
).properties(
    title='Dashboard Tren Durasi Pengiriman',
    width=800,
    height=400
)

st.altair_chart(chart)

# Tampilkan tabel data
st.write('Data Durasi Pengiriman:')
st.write(df)

# Group by month and year and count the number of purchases
trend_data_purchase = df.groupby(['purchase_year', 'purchase_month']).size().reset_index(name='purchase_count')

# Tampilkan plot dengan Altair untuk trend pembelian
chart_purchase = alt.Chart(trend_data_purchase).mark_line().encode(
    x='purchase_year:T',
    y='purchase_count:Q'
).properties(
    title='Dashboard Tren Pembelian',
    width=800,
    height=400
)

# Tampilkan plot dan tabel data
st.altair_chart(chart_purchase)

# Tampilkan tabel data
st.write('Data Durasi Pengiriman:')
st.write(df)
