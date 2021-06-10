import pandas as pd
import matplotlib.pyplot as plt
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
import math
import statistics
from python.found_criterior.methods_for_criterior.FeautureSelector import FeatureSelector

df = pd.read_csv('Data_with_class.csv')
df_class0 = df[df['CLASS'] == 0]
df_class1 = df[df['CLASS'] == 1]
df_class2 = df[df['CLASS'] == 2]
df_class3 = df[df['CLASS'] == 3]
# df.drop('INSTITUTEID', axis='columns', inplace=True)
# df.to_csv('Data_with_class.csv', index=False)
def normalizer(df):
    arr = []
    min_ = min(df)
    max_ = max(df)
    for i in range(len(df)):
        arr.append((df[i] - min_) / (max_ - min_))

    return arr


def replacements(df, param):
    arr = normalizer(df[param].values)
    df.loc[:, param] = arr
    return df

#     print(df.head(2))

df_class0.drop(df_class0[df_class0['COUNT_ACTIVITIES']>1000].index, inplace=True)
df_class1.drop(df_class1[df_class1['COUNT_ACTIVITIES']>1000].index, inplace=True)
df_class2.drop(df_class2[df_class2['COUNT_ACTIVITIES']>1000].index, inplace=True)
df_class3.drop(df_class3[df_class3['COUNT_ACTIVITIES']>1000].index, inplace=True)
df_class0 = replacements(df_class0, 'COUNT_ACTIVITIES')
df_class1 = replacements(df_class1, 'COUNT_ACTIVITIES')
df_class2 = replacements(df_class2, 'COUNT_ACTIVITIES')
df_class3 = replacements(df_class3, 'COUNT_ACTIVITIES')

# df_class0 = replacements(df_class0, 'INSTITUTEID')
# df_class1 = replacements(df_class1, 'INSTITUTEID')
# df_class2 = replacements(df_class2, 'INSTITUTEID')
# df_class3 = replacements(df_class3, 'INSTITUTEID')

df_class0 = replacements(df_class0, 'PUBLICATIONS')
df_class1 = replacements(df_class1, 'PUBLICATIONS')
df_class2 = replacements(df_class2, 'PUBLICATIONS')
df_class3 = replacements(df_class3, 'PUBLICATIONS')

df_class0 = replacements(df_class0, 'CONFERENCE')
df_class1 = replacements(df_class1, 'CONFERENCE')
df_class2 = replacements(df_class2, 'CONFERENCE')
df_class3 = replacements(df_class3, 'CONFERENCE')

df_class0 = replacements(df_class0, 'MEDALE')
df_class1 = replacements(df_class1, 'MEDALE')
df_class2 = replacements(df_class2, 'MEDALE')
df_class3 = replacements(df_class3, 'MEDALE')

df_class0 = replacements(df_class0, 'TYPEOFSCHOOL')
df_class1 = replacements(df_class1, 'TYPEOFSCHOOL')
df_class2 = replacements(df_class2, 'TYPEOFSCHOOL')
df_class3 = replacements(df_class3, 'TYPEOFSCHOOL')

df_class0.drop(df_class0[df_class0['COUNT_METTINGS']>140].index, inplace=True)
df_class1.drop(df_class1[df_class1['COUNT_METTINGS']>140].index, inplace=True)
df_class2.drop(df_class2[df_class2['COUNT_METTINGS']>140].index, inplace=True)
df_class3.drop(df_class3[df_class3['COUNT_METTINGS']>140].index, inplace=True)
df_class0 = replacements(df_class0, 'COUNT_METTINGS')
df_class1 = replacements(df_class1, 'COUNT_METTINGS')
df_class2 = replacements(df_class2, 'COUNT_METTINGS')
df_class3 = replacements(df_class3, 'COUNT_METTINGS')

df_class0.drop(df_class0[df_class0['TIME_AUDIO_MINUTES']>10000].index, inplace=True)
df_class1.drop(df_class1[df_class1['TIME_AUDIO_MINUTES']>10000].index, inplace=True)
df_class2.drop(df_class2[df_class2['TIME_AUDIO_MINUTES']>10000].index, inplace=True)
df_class3.drop(df_class3[df_class3['TIME_AUDIO_MINUTES']>10000].index, inplace=True)
df_class0 = replacements(df_class0, 'TIME_AUDIO_MINUTES')
df_class1 = replacements(df_class1, 'TIME_AUDIO_MINUTES')
df_class2 = replacements(df_class2, 'TIME_AUDIO_MINUTES')
df_class3 = replacements(df_class3, 'TIME_AUDIO_MINUTES')

df_class0.drop(df_class0[df_class0['TIME_VIDEO_MINUTES']>4000].index, inplace=True)
df_class1.drop(df_class1[df_class1['TIME_VIDEO_MINUTES']>4000].index, inplace=True)
df_class2.drop(df_class2[df_class2['TIME_VIDEO_MINUTES']>4000].index, inplace=True)
df_class3.drop(df_class3[df_class3['TIME_VIDEO_MINUTES']>4000].index, inplace=True)
df_class0 = replacements(df_class0, 'TIME_VIDEO_MINUTES')
df_class1 = replacements(df_class1, 'TIME_VIDEO_MINUTES')
df_class2 = replacements(df_class2, 'TIME_VIDEO_MINUTES')
df_class3 = replacements(df_class3, 'TIME_VIDEO_MINUTES')

df_class0.drop(df_class0[df_class0['SHARE_SCREEN_MINUTES']>2000].index, inplace=True)
df_class1.drop(df_class1[df_class1['SHARE_SCREEN_MINUTES']>2000].index, inplace=True)
df_class2.drop(df_class2[df_class2['SHARE_SCREEN_MINUTES']>2000].index, inplace=True)
df_class3.drop(df_class3[df_class3['SHARE_SCREEN_MINUTES']>2200].index, inplace=True)
df_class0 = replacements(df_class0, 'SHARE_SCREEN_MINUTES')
df_class1 = replacements(df_class1, 'SHARE_SCREEN_MINUTES')
df_class2 = replacements(df_class2, 'SHARE_SCREEN_MINUTES')
df_class3 = replacements(df_class3, 'SHARE_SCREEN_MINUTES')

df_class0 = replacements(df_class0, 'TET_A_TET_CALLS')
df_class1 = replacements(df_class1, 'TET_A_TET_CALLS')
df_class2 = replacements(df_class2, 'TET_A_TET_CALLS')
df_class3 = replacements(df_class3, 'TET_A_TET_CALLS')

df_class0.drop(df_class0[df_class0['MS_MESSAGES']>200].index, inplace=True)
df_class1.drop(df_class1[df_class1['MS_MESSAGES']>200].index, inplace=True)
df_class2.drop(df_class2[df_class2['MS_MESSAGES']>200].index, inplace=True)
df_class3.drop(df_class3[df_class3['MS_MESSAGES']>200].index, inplace=True)
df_class0 = replacements(df_class0, 'MS_MESSAGES')
df_class1 = replacements(df_class1, 'MS_MESSAGES')
df_class2 = replacements(df_class2, 'MS_MESSAGES')
df_class3 = replacements(df_class3, 'MS_MESSAGES')

# проверка
# columns = df_class3.columns[0:20]
# for i in range(len(columns)):
#     print(max(df_class3[columns[i]]))
data = df.loc[:,['COUNT_ACTIVITIES', 'SEX', 'BIRTHPLACE', 'ISOBCHAGA',
       'PUBLICATIONS', 'CONFERENCE', 'STUDACTIVE', 'CREATICEACTIVE',
       'SOCIALACTIVE', 'TYPEOFSCHOOL', 'COUNT_METTINGS',
       'TIME_AUDIO_MINUTES', 'TIME_VIDEO_MINUTES', 'SHARE_SCREEN_MINUTES',
       'TET_A_TET_CALLS', 'MS_MESSAGES']]

# from feature_selector import FeatureSelector
df_labels = df.loc[:,'CLASS'].values
# Признаки - в train, метки - в train_labels
fs = FeatureSelector(data = data, labels = df_labels)
# task – classification или regression в зависимости от задачи;
# eval_metric – метрика для ранней остановки (не требуется, если ранняя остановка отключена);
# n_iterations – количество прогонов обучения для усреднения важности;
# early_stopping – включение/отключение ранней остановки.
fs.identify_zero_importance(task = 'regression',
                            eval_metric = 'auc',
                            n_iterations = 10,
                             early_stopping = True)

zero_importance_features = fs.ops['zero_importance']

X_MAJOR = 7


def count_sum_major_and_minor_index(df):
    major_features = ['COUNT_ACTIVITIES', 'SHARE_SCREEN_MINUTES', 'TIME_VIDEO_MINUTES',
                      'TIME_AUDIO_MINUTES', 'COUNT_METTINGS', 'MS_MESSAGES', 'BALLSTOTAL']

    sum_major = []
    list_index = df.index
    for i in range(len(list_index)):
        sum_major.append((sum(df.loc[list_index[i], major_features])))

    count = 0

    return sum_major


def criterior_success(sum_major):
    return (sum_major / X_MAJOR)


sums_class0 = count_sum_major_and_minor_index(df_class0)
sums_class1 = count_sum_major_and_minor_index(df_class1)
sums_class2 = count_sum_major_and_minor_index(df_class2)
sums_class3 = count_sum_major_and_minor_index(df_class3)

crit_succ_ub = statistics.mean(sums_class3)
crit_cl_succ_ub = statistics.mean(sums_class1)
crit_no_succ_ub = statistics.mean(sums_class0)


def classification(sums_value, crit_succ_ub ,crit_cl_succ_ub, crit_no_succ_ub):
    arr_succ_words = []
    arr_succ_int = []
    for i in range(len(sums_value)):
        if (sums_value[i]>=crit_succ_ub):
            arr_succ_words.append('SUCCESS')
            arr_succ_int.append(2)
#             print('SUCCESS')
        elif sums_value[i] >=crit_cl_succ_ub:
            arr_succ_words.append('CLOSE TO SUCCESS')
            arr_succ_int.append(1)
# #             print('CLOSE TO SUCCESS')
        elif sums_value[i] >=crit_no_succ_ub:
            arr_succ_words.append('NO SUCCESS')
            arr_succ_int.append(0)
#             print('NO TO SUCCESS')
        else:
            arr_succ_words.append('NO SUCCESS')
            arr_succ_int.append(0)
    return arr_succ_words, arr_succ_int

cl0_words, cl0_int = classification(sums_class0,crit_succ_ub, crit_cl_succ_ub, crit_no_succ_ub)
cl1_words, cl1_int = classification(sums_class1,crit_succ_ub, crit_cl_succ_ub, crit_no_succ_ub)
cl2_words, cl2_int = classification(sums_class2,crit_succ_ub, crit_cl_succ_ub, crit_no_succ_ub)
cl3_words, cl3_int = classification(sums_class3,crit_succ_ub, crit_cl_succ_ub, crit_no_succ_ub)


df_class0.insert(21, "SUCCESS_METRICS_WORDS", cl0_words, True)
df_class0.insert(21,"SUCCESS_METRICS_NUMBERS", cl0_int, True)

df_class1.insert(21, "SUCCESS_METRICS_WORDS", cl1_words, True)
df_class1.insert(21,"SUCCESS_METRICS_NUMBERS", cl1_int, True)
df_class2.insert(21, "SUCCESS_METRICS_WORDS", cl2_words, True)
df_class2.insert(21,"SUCCESS_METRICS_NUMBERS", cl2_int, True)
df_class3.insert(21, "SUCCESS_METRICS_WORDS", cl3_words, True)
df_class3.insert(21,"SUCCESS_METRICS_NUMBERS", cl3_int, True)

new_df = pd.concat([df_class0, df_class1, df_class2, df_class3])
new_df.sort_index(inplace=True)
new_df.to_csv('New_data.csv', index=False)