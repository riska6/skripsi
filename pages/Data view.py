# Import Library
import streamlit as st
import pandas as pd
from openpyxl import excel
import os

st.subheader("Halaman Excel")
st.write(
            """
            Pada halaman ini, akan menampilkan bagaimana data pasien yang akan digunakan pada website.
            """
        )

df = pd.read_csv("./data/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hello world!")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app
