# Import Library
import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
import os

st.title("View Data")
st.subheader("Pengaturan Visualisasi")

#setup file upload
uploaded_file = st.file_uploader(label="Upload your excel or csv file.",
                        type=['csv', 'xlsx'])

if uploaded_file is not None:
  try:
    df = pd.read_csv(uploaded_file)
  except:
    try:
      df = pd.read_excel(uploaded_file)
    except Exception as e:
      st.write("Error Upload File")
    
try:
  st.write(df)
  numeric_columns = list(df.columns)
except Exception as e:
  st.write('Error Reading Columns')

chart_select = st.selectbox(
    label="Pilih tipe chart",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot'])

if chart_select == 'Scatterplots':
  st.subheader("Scatterplot Settings")
  try:
    x_values = st.selectbox('X axis', options=np.append('', numeric_columns))
    y_values = st.selectbox('Y axis', options=np.append('', numeric_columns))
    if x_values=='':
      print("Y")
      plot = px.scatter(data_frame=df, x=x_values, y=y_values)
      st.plotly_chart(plot)
    else:
      print(x_values)
      plot = px.scatter(data_frame=df, x=x_values, y=y_values)
      st.plotly_chart(plot)
    
    
  except Exception as e:
    print(e)