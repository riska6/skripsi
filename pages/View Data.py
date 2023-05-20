# Import Library
import streamlit as st
import pandas as pd
import os

st.title("View Data")
st.sidebar.subheader("Pengaturan Visualisasi")

#setup file upload
st.sidebar.file_uploader(label="Upload your excel or csv file.")
