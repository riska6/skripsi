import streamlit as st
import webbrowser

 st.write("url = 'https://riska6-skripsi-homepage-dgg9jf.streamlit.app/contact")

if st.button('Open browser'):
    webbrowser.open_new_tab(url)

st.set_page_config(
    page_title="Selamat Datang di Website Kombinasi AHC & K-Means",
    page_icon="👋",
)

st.title("Halaman Utama")
st.sidebar.success("Pilih halaman diatas.")

if "riska" not in st.session_state:
    st.session_state["riska"] = ""

my_input = st.text_input("Masukkan Username", st.session_state["riska"])
submit = st.button("Submit")
if submit:
    st.session_state["riska"] = my_input
    st.write("Selamat Datang, ", my_input)
