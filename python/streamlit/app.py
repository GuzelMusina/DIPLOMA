import streamlit as st
import pandas as pd
import os

Text1 = "Пожалуйста загрузите файлы из электронного университета КФУ \n с названиями  'Student.csv', 'Marks.csv', \n" \
        "из Microsoft Teams 'MicrosoftTeamsActivity.csv' \n" \
        "из Moodle 'MoodleLogs.csv', 'MoodleStudents.csv"
st.text(Text1)

uploaded_file = st.file_uploader("Загрузите файлы", type=['xls','csv'], accept_multiple_files=True)
if uploaded_file is not None:
    for i in range(len(uploaded_file)):
        file_details = {"FileName":uploaded_file[i].name,"FileType":uploaded_file[i].type,
                        "FileSize":uploaded_file[i].size}
        st.write(file_details)

Text2 = "Если вы загрузили 5 файлов, пожалуйста, нажмите 'продолжить'"
st.text(Text2)

if len(uploaded_file)==5:
    if st.button("Продолжить"):
        st.text("Обработка данных... подождите")
else:
    st.text("Загрузите недостающие файлы")

