import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import base64
from python.predictor.NN import NN

plt.style.use('fivethirtyeight')

from sklearn.model_selection import train_test_split


from plotly.offline import init_notebook_mode
import plotly.graph_objs as go

import python.helpers.Reader as Reader
import python.found_criterior.methods_for_criterior.FoundCriterior as foundCriterior
import python.found_criterior.methods_for_criterior.FeautureSelector as featureSelector

init_notebook_mode(connected=True)

reader = Reader()

def highlight_classes(x):
    return ['background-color: yellow' if v == x.max() else '' for v in x]


menu = st.sidebar.markdown("# Меню")
select_event_add_and_refactor_and_clustering = st.sidebar.selectbox('Шаг 1',
                                                                    ['',
                                                                     'Загрузить, обработать, кластеризовать данные'])

select_event_visualize_data = 0
if select_event_add_and_refactor_and_clustering == 'Загрузить, обработать, кластеризовать данные':
    Text1 = "Пожалуйста загрузите файлы из электронного университета КФУ \n с названиями  *'Student.csv'*, *'Marks.csv'*, \n" \
            "из Microsoft Teams *'MicrosoftTeamsActivity.csv'* \n" \
            "из Moodle *'MoodleLogs.csv', 'MoodleStudents.csv'*"
    st.markdown(Text1)

    file_names = []
    uploaded_file = st.file_uploader("Загрузите файлы", type=['xls', 'csv'], accept_multiple_files=True)
    if uploaded_file is not None:
        for i in range(len(uploaded_file)):
            file_details = {"FileName": uploaded_file[i].name, "FileType": uploaded_file[i].type,
                            "FileSize": uploaded_file[i].size}
            file_names.append(uploaded_file[i].name)
            if uploaded_file[i].name == "Students.csv":
                dataset_students_eor = reader.readCSV(uploaded_file[i])
            elif uploaded_file[i].name == "Marks.csv":
                dataset_marks_eor = reader.readCSV(uploaded_file[i])
            elif uploaded_file[i].name == "MicrosoftTeamsActivity.csv":
                dataset_msteams = reader.readCSV(uploaded_file[i])
            elif uploaded_file[i].name == "MoodleLogs.csv":
                dataset_logs_moodle = reader.readCSV(uploaded_file[i])
            elif uploaded_file[i].name == "MoodleStudents.csv":
                dataset_students_moodle = reader.readCSVWithSeparator(uploaded_file[i])

            st.write(file_details)

    # mainChangers = MainChangers(dataset_students_eor, dataset_marks_eor, dataset_msteams,
    #                             dataset_logs_moodle,dataset_students_moodle)

    if len(uploaded_file) != 5:
        st.error("Загрузите недостающие файлы (5)")
    else:
        st.markdown("### Вы можете посмотреть содержимое каждого файла, для этого выберите его из списка ниже")
        select_event_add_and_refactor_and_clustering = st.selectbox('Название загруженных файлов', file_names)
        if select_event_add_and_refactor_and_clustering == "Students.csv":
            st.text(dataset_students_eor.head())
        elif select_event_add_and_refactor_and_clustering == "Marks.csv":
            st.text(dataset_marks_eor.head())
        elif select_event_add_and_refactor_and_clustering == "MicrosoftTeamsActivity.csv":
            st.text(dataset_msteams.head())
        elif select_event_add_and_refactor_and_clustering == "MoodleLogs.csv":
            st.text(dataset_logs_moodle.head())
        elif select_event_add_and_refactor_and_clustering == "MoodleStudents.csv":
            st.text(dataset_students_moodle.head())

        if st.button("Обработать данные"):
            df = pd.read_csv('python/found_criterior/Data_with_class.csv')
            st.dataframe(df.style.apply(highlight_classes, subset=['BALLSTOTAL']))

        if st.button("Кластеризоать"):
            select_event_add_and_refactor_and_clustering = "Кластризовать данные"
            df = pd.read_csv('python/found_criterior/New_data.csv')
            st.markdown("Даные кластеризованы по методу T-SNE")
            st.markdown("### В меню вы можете выбрать пункт из списка 'Посмотреть данные' для того,"
                        "чтобы подробнее ознакомиться с данными")

    select_event_visualize_data = st.sidebar.selectbox('Посмотреть данные',
                                                       ['', 'Матрица корреляции', 'Зависимость между тремя признаками',
                                                        'Диапазон принимающих значений'])

df = pd.read_csv('python/found_criterior/New_data.csv')
if select_event_visualize_data == 'Матрица корреляции':
    plt.rcParams['figure.figsize'] = (40, 20)
    sns.heatmap(df.corr(), cmap='PuBu', annot=True)
    plt.title('Heatmap for the Data', fontsize=20)
    st.pyplot(plt)

elif select_event_visualize_data == 'Зависимость между тремя признаками':
    options = st.multiselect('Посмотреть зависимость между признаками', df.columns, help="Выберите три признака")
    if len(options) != 3:
        st.markdown("Пожалуйста выберите три признака")
    else:
        st.write('You selected:', options)

        trace = go.Scatter3d(
            x=df[options[0]],
            y=df[options[1]],
            z=df[options[2]],
            mode='markers',
            marker=dict(
                size=12,
                color=df[options[2]],  # set color to an array/list of desired values
                colorscale='Viridis',  # choose a colorscale
                opacity=0.8
            )
        )
        data = [trace]
        layout = go.Layout(
            title='зависимость между ',
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0
            ),
            scene=dict(
                xaxis=dict(title=options[0]),
                yaxis=dict(title=options[1]),
                zaxis=dict(title=options[2])
            )
        )
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

elif select_event_visualize_data == 'Диапазон принимающих значений':

    df.hist(figsize=(24, 20))
    st.pyplot(plt)

select_event_success_criterior = st.sidebar.selectbox('Шаг 2',
                                                      ['', 'Определить критерии успешности'])
if select_event_success_criterior == 'Определить критерии успешности':

    with st.spinner('Подождите немного...'):
        time.sleep(5)
    foundCriterior
    st.success('Готово!')
    st.markdown("### Самые важные признаки: ")
    featureSelector.identify_zero_importance()

select_event_success_criterior = st.sidebar.selectbox('Шаг 3',
                                                      ['', 'Прогнозирвование успешности'])
if select_event_success_criterior == 'Прогнозирвование успешности':

    TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    Predictors = ['COUNT_ACTIVITIES', 'COUNT_METTINGS', 'SHARE_SCREEN_MINUTES', 'TIME_VIDEO_MINUTES',
                  'TIME_AUDIO_MINUTES', 'MS_MESSAGES', 'TET_A_TET_CALLS', 'TYPEOFSCHOOL',
                  'PUBLICATIONS']

    X = df[Predictors].values
    y = df[TargetVariable].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    ACC_NN = NN(X_train, X_test, y_train, y_test)

    # df_now = pd.read_csv('python/found_criterior/Data_with_class.csv')
    df_orig = pd.read_csv('data/Final Wave/Final.csv')
    df_orig.drop(df_orig[df_orig.BALLSTOTAL == -1].index, inplace=True)

    df_orig.drop(df_orig[df_orig['COUNT_ACTIVITIES'] > 1000].index, inplace=True)
    df_orig.drop(df_orig[df_orig['COUNT_METTINGS'] > 140].index, inplace=True)
    df_orig.drop(df_orig[df_orig['TIME_AUDIO_MINUTES'] > 10000].index, inplace=True)
    df_orig.drop(df_orig[df_orig['TIME_VIDEO_MINUTES'] > 4000].index, inplace=True)
    df_orig.drop(df_orig[df_orig['SHARE_SCREEN_MINUTES'] > 2000].index, inplace=True)
    df_orig.sort_index(inplace=True)

    id = st.text_input("Введите id студента: ", help='Посмотреть id вы можете загрузив файл "SPISOK.csv"')
    temp_file = pd.DataFrame(df_orig.loc[:, 'FIO'])
    csv = temp_file.to_csv()
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Скачать файл SPISOK.csv</a>'
    st.markdown(href, unsafe_allow_html=True)

    if id != '':
        st.write(df_orig.loc[int(id), :])
        st.write(df.loc[int(id), 'SUCCESS_METRICS_WORDS'])

st.markdown("Вы также можете выбрать собственные параметры")
col1, col2, col3 = st.beta_columns(3)
with col1:
    count_activities = st.slider('Активность в Moodle', max_value=1000, min_value=1)
    count_meetings = st.slider('Кличество встреч в Microsoft Teams', max_value=140, min_value=1)
    time_audio_minutes = st.slider('Кличество минут аудио сообщений в Microsoft Teams', max_value=10000, min_value=1)
    time_video_minutes = st.slider('Кличество минут видео сообщений в Microsoft Teams', max_value=4000, min_value=1)
    share_screen_minutes = st.slider('Кличество минут "поделиться экраном" в Microsoft Teams', max_value=2000,
                                     min_value=1)
with col2:
    st.markdown("Пол")
    sex_f = st.checkbox('Ж')
    sex_m = st.checkbox('М')
    country = st.selectbox('Страна', ['Россиия', 'Не россиия'])
    school = st.selectbox('Тип учебного учреждения, который закончил студент', ['Школа', 'Вуз', 'Лицей', 'Гимназия',
                                                                                'Колледж', 'Техникум', 'Прочее'])
with col3:
    publication = st.checkbox('Имеются публикации')
    conference = st.checkbox('Участвовал в конференциях')
    studactiv = st.checkbox('Участвовал в студенческих активностях')

predict = st.button("Предсказать")
arr = []
arr.append(count_activities)
arr.append(count_meetings)
arr.append(time_audio_minutes)
arr.append(time_video_minutes)
arr.append(sex_f)
arr.append(sex_m)
arr.append(country)
arr.append(school)
arr.append(publication)
arr.append(conference)
arr.append(studactiv)

success_value = ACC_NN.predict(arr)

if predict:
    if success_value == 0:
        st.error("Студент не успешный")
    elif success_value == 1:
        st.success("Студент близок к успешному")
    elif success_value == 2:
        st.success("Студент успешный")
