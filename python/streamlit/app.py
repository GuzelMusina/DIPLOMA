import streamlit as st
import pandas as pd
import os

uploaded_file = st.file_uploader("Upload Files",type=['xls','csv'], accept_multiple_files=True)
if uploaded_file is not None:
    for i in range(len(uploaded_file)):
        file_details = {"FileName":uploaded_file[i].name,"FileType":uploaded_file[i].type,
                        "FileSize":uploaded_file[i].size}
        st.write(file_details)
