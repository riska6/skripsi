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
df = pd.read_excel("./pages/DATA PASIEN DIABETES FIX.xlsx")  # read a excel file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
