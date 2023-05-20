# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

  # Add some matplotlib code !
  fig, ax = plt.subplots()
  df.hist(
    bins=8,
    column="Age",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
  st.write(fig)
