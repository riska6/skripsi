import streamlit as st


st.title("View Data")

st.write("Pengelompokan data pasien yang dilakukan pada suatu instansi kesehatan masih belum secara total menganalisa data yang memiliki karakteristik gejala dengan tingkat Diabetes yang mirip. Untuk mengetahui apakah pengelompokan dengan karakteristik yang mirip menggunakan data pasien, dilakukan pengelompokan data menggunakan penggabungan lebih dari satu metode, yaitu metode K-Means dan AHC (Agglomerative Hierarchical Clustering). Berikut adalah data pasien tersebut:", st.session_state["my_input"])
