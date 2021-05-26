import html as html
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

# for interactive visualizations
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from plotly import tools

init_notebook_mode(connected=True)
import plotly.figure_factory as ff

from IPython.display import HTML


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
status = False
menu = st.sidebar.markdown("# Меню")
select_event = st.sidebar.selectbox('Загрузить и обработать данные',
                                    ['Показать данные', 'Кластризовать данные',
                                     'Посмотреть зависимость между признаками',
                                     'Поиск критериев успешности', 'Прогнозирование'])

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

Text2 = "Если вы загрузили 5 файлов, пожалуйста, нажмите 'продолжить'"
st.markdown(Text2)

if len(uploaded_file) != 1:
    st.markdown("Загрузите недостающие файлы")
    # else:
if st.button("Продолжить"):
    status = True
    st.markdown("Вы можете посмотреть содержимое каждого файла, для этого выберите его из списка ниже")
    select_event = st.selectbox('Название загруженных файлов', file_names)
if select_event == "Students.csv":
    st.text(dataset_students_eor.head())
elif select_event == "Marks.csv":
    st.text(dataset_marks_eor.head())
elif select_event == "MicrosoftTeamsActivity.csv":
    st.text(dataset_msteams.head())
elif select_event == "MoodleLogs.csv":
    st.text(dataset_logs_moodle.head())
elif select_event == "MoodleStudents.csv":
    st.text(dataset_students_moodle.head())


def highlight_max(data, color='yellow'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)


if st.button("Обработать данные"):
    if status == False:
        df = pd.read_csv('python_pack/found_criterior/Data_with_class.csv')
        st.dataframe(df.style.highlight_max(axis=0))
    else:
        st.error("Загрузите данные")

if st.button("Кластеризоать"):
    select_event = "Кластризовать данные"
    df = pd.read_csv('python_pack/found_criterior/New_data.csv')
    st.markdown("Даные кластеризованы по методу T-SNE")

df = pd.read_csv('python_pack/found_criterior/New_data.csv')

if st.button("Посмотреть матрицу корреляции"):
    plt.rcParams['figure.figsize'] = (40, 20)
    sns.heatmap(df.corr(), cmap='PuBu', annot=True)
    plt.title('Heatmap for the Data', fontsize=20)
    st.pyplot(plt)

options = st.multiselect('Посмотреть зависимость между признаками', df.columns, help="Выберите три признака")
st.write('You selected:', options)

trace = go.Scatter3d(
    x=df[options[0]],
    y=df[options[1]],
    z=df[options[2]],
    mode='markers',
    opacity=0.8
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

# py.iplot(fig)
# fig.write_html("3d_cluster.html")

# foundCriterior
# import altair as alt
#
#
# try:
#     df = get_UN_data()
#     countries = st.multiselect(
#         "Choose countries", list(df.index), ["China", "United States of America"]
#     )
#     if not countries:
#         st.error("Please select at least one country.")
#     else:
#         data = df.loc[countries]
#         data /= 1000000.0
#         st.write("### Gross Agricultural Production ($B)", data.sort_index())
#
#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=["index"]).rename(
#             columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#         )
#         chart = (
#             alt.Chart(data)
#                 .mark_area(opacity=0.3)
#                 .encode(
#                 x="year:T",
#                 y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                 color="Region:N",
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#
#         Connection error: %s
#     """
#         % e.reason
#     )
#

# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.

# iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
# separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

# # Non-interactive elements return a placeholder to their location
# # in the app. Here we're storing progress_bar to update it later.
# progress_bar = st.sidebar.progress(0)
#
# # These two elements will be filled in later, so we create a placeholder
# # for them using st.empty()
# frame_text = st.sidebar.empty()
# image = st.empty()
#
# m, n, s = 960, 640, 400
# x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
# y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

# # We clear elements by calling empty on them.
# progress_bar.empty()
# frame_text.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")
