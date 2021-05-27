import html as html
import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from plotly.subplots import make_subplots

plt.style.use('fivethirtyeight')
# Split the data into training and testing set
from sklearn.model_selection import train_test_split

# for interactive visualizations
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from plotly import tools
import sklearn.metrics as metrics
init_notebook_mode(connected=True)
import plotly.figure_factory as ff

from IPython.display import HTML

# from python_pack.predictor.Predictor import Predictors

# import python_pack.found_criterior.methods_for_criterior.FoundCriterior as foundCriterior
# from python_pack.changers.main_changers import MainChangers
class Reader(object):

    def readCSV(self, path):
        dataset = pd.read_csv(path)
        return dataset

    def readCSVWithSeparator(self, path):
        dataset = pd.read_csv(path, sep=';')
        return dataset


reader = Reader()

def NN(X_train, X_test, y_train, y_test):

    INPUT = 9
    # importing the libraries
    from keras.models import Sequential
    from keras.layers import Dense

    # create ANN model
    model = Sequential()

    # Defining the Input layer and FIRST hidden layer, both are same!
    model.add(Dense(units=36, input_dim=INPUT, kernel_initializer='normal', activation='linear'))

    # Defining the Second layer of the model
    # after the first layer we don't have to specify input_dim as keras configure it automatically
    model.add(Dense(units=72, kernel_initializer='normal', activation='linear'))
    model.add(Dense(units=72, kernel_initializer='normal', activation='linear'))
        # The output neuron is a single fully connected node
    # Since we will be predicting a single number
    model.add(Dense(1, kernel_initializer='normal'))

    # Compile the network :
    model.compile(loss='mean_absolute_error', optimizer='RMSProp', metrics=['mean_absolute_error'])
    model.summary()

    # Compiling the model
    model.compile(loss='mean_absolute_error', optimizer='RMSProp')

    # Fitting the ANN to the Training set
    model.fit(X_train, y_train, batch_size=20, epochs=50)

    predict = model.predict(X_test)
    predict = abs(predict.ravel())
    expect = y_test.ravel()
    for i in range(len(predict)):
        predict[i] = int(round(predict[i]))
    expect = y_test.ravel()

    mae = metrics.mean_absolute_error(expect, predict)
    mse = metrics.mean_squared_error(expect, predict)
    rmse = np.sqrt(mse)  # or mse**(0.5)
    r2 = metrics.r2_score(expect, predict)

    print("Results of sklearn.metrics:")
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R-Squared:", r2)

    st.write(metrics.classification_report(expect, predict))
    st.write(metrics.confusion_matrix(expect, predict))

    # return accuracy_score(expect, predict)

menu = st.sidebar.markdown("# Меню")
select_event_add_and_refactor_and_clustering = st.sidebar.selectbox('Шаг 1',
                                                                    ['', 'Загрузить, обработать, кластеризовать данные'])

select_event_visualize_data = 0
if select_event_add_and_refactor_and_clustering == 'Загрузить, обработать, кластеризовать данные':
    Text1 = "Пожалуйста загрузите файлы из электронного университета КФУ \n с названиями  *'Student.csv'*, *'Marks.csv'*, \n" \
            "из Microsoft Teams *'MicrosoftTeamsActivity.csv'* \n" \
            "из Moodle *'MoodleLogs.csv', *'MoodleStudents.csv'*"
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
            df = pd.read_csv('python_pack/found_criterior/Data_with_class.csv')
            st.dataframe(df.style.highlight_max(axis=0))

        if st.button("Кластеризоать"):
            select_event_add_and_refactor_and_clustering = "Кластризовать данные"
            # df = pd.read_csv('python_pack/found_criterior/New_data.csv')
            st.markdown("Даные кластеризованы по методу T-SNE")
            st.markdown("### В меню вы можете выбрать пункт из списка 'Посмотреть данные' для того,"
                        "чтобы подробнее ознакомиться с данными")

    select_event_visualize_data = st.sidebar.selectbox('Посмотреть данные',
                                                       ['', 'Матрица корреляции', 'Зависимость между тремя признаками',
                                                        'Диапазон принимающих значений'])

df = pd.read_csv('python_pack/found_criterior/New_data.csv')
if select_event_visualize_data == 'Матрица корреляции':
    plt.rcParams['figure.figsize'] = (40, 20)
    sns.heatmap(df.corr(), cmap='PuBu', annot=True)
    plt.title('Heatmap for the Data', fontsize=20)
    st.pyplot(plt)

elif select_event_visualize_data == 'Зависимость между тремя признаками':
    options = st.multiselect('Посмотреть зависимость между признаками', df.columns, help="Выберите три признака")
    if len(options)!=3:
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
if select_event_success_criterior=='Определить критерии успешности':
    # foundcriterior()
    # major_features = ['COUNT_ACTIVITIES', 'SHARE_SCREEN_MINUTES', 'TIME_VIDEO_MINUTES',
    #                   'TIME_AUDIO_MINUTES', 'COUNT_METTINGS', 'MS_MESSAGES']
    with st.spinner('Подождите немного...'):
        time.sleep(5)
    st.success('Готово!')
    st.markdown("### Самые важные признаки: ")
    st.markdown("1. COUNT_ACTIVITIES")
    st.markdown("2. SHARE_SCREEN_MINUTES")
    st.markdown("3. TIME_VIDEO_MINUTES")
    st.markdown("4. TIME_AUDIO_MINUTES")
    st.markdown("5. COUNT_METTINGS")
    st.markdown("6. TYPEOFSCHOOL")

select_event_success_criterior = st.sidebar.selectbox('Шаг 3',
                                                       ['', 'Прогнозирвование успешности'])
if select_event_success_criterior=='Прогнозирвование успешности':

    TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    Predictors = ['COUNT_ACTIVITIES', 'COUNT_METTINGS', 'SHARE_SCREEN_MINUTES', 'TIME_VIDEO_MINUTES',
                  'TIME_AUDIO_MINUTES', 'MS_MESSAGES', 'TET_A_TET_CALLS', 'TYPEOFSCHOOL',
                  'PUBLICATIONS']

    X = df[Predictors].values
    y = df[TargetVariable].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    ACC_NN = NN(X_train, X_test, y_train, y_test)

df_now = pd.read_csv('python_pack/found_criterior/Data_with_class.csv')
df_orig = pd.read_csv('data/Final Wave/Final.csv')
df_orig.drop(df_orig[df_orig.BALLSTOTAL == -1].index, inplace=True)

df_orig.drop(df_orig[df_orig['COUNT_ACTIVITIES']>1000].index, inplace=True)
df_orig.drop(df_orig[df_orig['COUNT_METTINGS']>140].index, inplace=True)
df_orig.drop(df_orig[df_orig['TIME_AUDIO_MINUTES']>10000].index, inplace=True)
df_orig.drop(df_orig[df_orig['TIME_VIDEO_MINUTES']>4000].index, inplace=True)
df_orig.drop(df_orig[df_orig['SHARE_SCREEN_MINUTES']>2000].index, inplace=True)
df_orig.sort_index(inplace=True)

# st.dataframe(df_orig)
# st.dataframe(df)

# st.write(len(df_orig), len(df))
