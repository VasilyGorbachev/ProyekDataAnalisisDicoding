import pandas as pd
import matplotlib.p as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

customers_df = pd.read_csv("customers_dataset.csv")
geolocation_df=pd.read_csv("geolocation_dataset.csv")
order_items_df = pd.read_csv("order_items_dataset.csv")
order_payments_df = pd.read_csv("order_payments_dataset.csv")
order_df = pd.read_csv("orders_dataset.csv")
product_category_df =  pd.read_csv("product_category_name_translation.csv")
product_df = pd.read_csv("products_dataset.csv")
seller_df = pd.read_csv("sellers_dataset.csv")

def new_orderpayment (df) :
    order_payments_df.groupby(by="payment_type").agg({
    "order_id": "nunique"
},inplace=True)
    
def top5(df):
    customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).head(5)

d1 = pd.read_csv("d1.csv")
d2 = pd.read_csv("d2.csv")

#filter
min_date = d1["order_purchase_timestamp"].min()
max_date = d1["order_purchase_timestamp"].max()

##DASHBOARD##
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
#    start_date, end_date = st.date_input(
#        label='Rentang Waktu',min_value=min_date,
#        max_value=max_date,
#        value=[min_date, max_date]
#   )
#    main_df = d2[(d2["order_approved_at"] >= str(start_date)) & 
#                (d2["order_approved_at"] <= str(end_date))]
    
st.title('Data Analysis with Python')
st.header('Proyek Akhir (mine version) :rocket:')
st.subheader('Top State by Order')

fig, ax = plt.subplots(figsize=(20, 10))

bystate_df = d2.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).reset_index().head(5)
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

colors_ = ["#F7EF8A", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
ax.set_title("Top 5 States by Order", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

st.subheader('Top Payment Method')

fig, ax = plt.subplots(figsize=(20, 10))

bypayment_df = d1.groupby(by="payment_type").customer_id.nunique().reset_index()
bypayment_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

colors_ = ["#F7EF8A", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="customer_count",
    x="payment_type",
    data=bypayment_df.sort_values(by="customer_count", ascending=False)
)
ax.set_title("Total Orders by Payment", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

st.caption('Copyright (c) Vasily 2023')
