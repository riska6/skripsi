# Import Library
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

st.subheader("Halaman Excel")
st.write(
            """
            Pada halaman ini, akan menampilkan bagaimana data pasien yang akan digunakan pada website.
            """
        )
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  st.write(df)
  st.write(fig)
