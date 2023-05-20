# Import Library
import streamlit as st
import pandas as pd
import os

st.title("View Data")
st.sidebar.subheader("Pengaturan Visualisasi")

#setup file upload
upload_file = st.sidebar.file_uploader(label="Upload your excel or csv file.",
                        type=['csv', 'xlsx'])
global df 
if uploaded_file is not None:
  print(uploaded_file)
  print("hello")
  try:
    df = pd.read_excel(uploaded_file)
  except Exception as e:
    print(e)
    df = pd.read_csv(uploaded_file)
    
try:
  st.write(df)
except Exception as e:
  print(e)
  st.write("Tolong upload file yang benar.")

  chart_select = st.slidebar.selectbox(
    label="Pilih tipe chart",
    options=["Scatterplots", "Lineplots", "Histogram", "Boxplot"])

if chart_select == "Scatterplots":
  st.sidebar.subheader("Scatterplot Settings")
  x_values = st.sidebar.selectbox('X axis', options=['a', 'b'])
