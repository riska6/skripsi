# Import Library
import streamlit as st
import pandas as pd
import os

st.title("View Data")
st.write(
            """
            Pada halaman ini, akan menampilkan bagaimana data pasien yang akan digunakan pada website.
            """
        )

df = pd.read_excel("DATA PASIEN DIABETES FIX.xlsx")
st.dataframe(df)
