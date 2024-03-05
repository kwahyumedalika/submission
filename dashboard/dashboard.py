import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import streamlit as st

histo_item_df = pd.read_csv("histo_item.csv")
pie_df = pd.read_csv("pie.csv")

st.title('Dashboard Ceria :sparkles:')

with st.sidebar:
    
    st.text('Kadek Wahyu Medalika Manik Segara')
tab1, tab2 = st.tabs(["Visualisasi 1", "Visualisasi 2"])
 
with tab1:
    st.header("Top 10 Produk Terlaris")
    histo_item_df.sort_values(by='order_item_id', inplace=True)

    fig, ax = plt.subplots()
    ax.barh(y=histo_item_df["product_id"], width=histo_item_df["order_item_id"])
    ax.set_xlabel("Jumlah Terjual")
    ax.set_title("Top 10 Produk Terlaris")

    st.pyplot(fig)
 
with tab2:
    st.header("Payment Type")
    fig, ax = plt.subplots()
    ax.pie(
        x=pie_df["Count"],
        labels=pie_df["Payment Type"],
        autopct='%1.1f%%',
        wedgeprops={'width': 0.9}
    )
    ax.set_title("Payment Type")
    
    st.pyplot(fig)

