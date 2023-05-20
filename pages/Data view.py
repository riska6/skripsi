# Import Library
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import os

st.title("View Data")
st.write(
            """
            Pada halaman ini, akan menampilkan bagaimana data pasien yang akan digunakan pada website.
            """
        )
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Product", ["BFR CORPORATE", 'BFR mikro', 'BFR Consumer', 'BRF'], 
        icons=['play', 'play'], menu_icon="cast", default_index=1)
    selected
    print(selected)
df = pd.read_excel("DATA PASIEN DIABETES FIX.xlsx")
st.dataframe(df)
