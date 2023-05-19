# Import Library
import streamlit as st
import pandas as pd
import os

st.subheader("Halaman Excel")
st.write(
            """
            Pada halaman ini, akan menampilkan bagaimana data pasien yang akan digunakan pada website.
            """
        )

# Method atau fungsi save
def save_upload(uploadedfile):
    with open(os.path.join("Documents/DataCsv",uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        return st.success("File berhasil disave: {} in Documents".format(uploadedfile.name))

data_file = st.file_uploader("Upload Excel",type=["xlsx"])
if data_file is not None:
    st.write(type(data_file))
    file_details = {"Filename":data_file.name,
    "FileType":data_file.type,"FileSize":data_file.size}
    st.write(file_details)
    df = pd.read_xlsx(data_file)
    st.dataframe(df)

    # Save File
    save_upload(data_file)
