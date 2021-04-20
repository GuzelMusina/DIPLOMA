import pandas as pd
pd.set_option('display.max_columns', None)

class Refactor(object):

    df = pd.read_csv('Data_with_class.csv')
    df_class0 = df[df['CLASS']==0]
    df_class1 = df[df['CLASS']==1]
    df_class2 = df[df['CLASS']==2]
    df_class3 = df[df['CLASS']==3]

    for i in range(len(df)):
        if df.loc[i, 'SEX'] == 2:
            df.loc[i, 'SEX'] =0
    for i in range(len(df)):
        if df.loc[i, 'MARTIALSTATUSID'] == 2:
            df.loc[i, 'MARTIALSTATUSID'] =0
    for i in range(len(df)):
        if df.loc[i, 'STUDACTIVE'] == 2:
            df.loc[i, 'STUDACTIVE'] = 1
    for i in range(len(df)):
        if df.loc[i, 'CREATICEACTIVE'] == 2:
            df.loc[i, 'CREATICEACTIVE'] = 1

    names = df.columns

    mess_arr = []
    for j in range(len(df)):
        summ = df['CHANNEL_MESSAGE'][j] +  df['PUBLISHED_MESSAGES'][j] + df['CHAT_MESSAGES'][j] + df['URGENT_MESSAGES'][j]
        mess_arr.append(summ)
    df.insert(len(names), 'MS_MESSAGES', mess_arr, True)


    df.drop(['KINDTRAINING', 'TYPETRAINING', 'CATEGORYID',
             'QUALIFICATIONTYPE', 'STUDTYPE_ID', 'HOW_MUCH_METTINGS_WERE_ORGANIZE',
             'CHANNEL_MESSAGE', 'PUBLISHED_MESSAGES', 'CHAT_MESSAGES', 'URGENT_MESSAGES'
            ], axis='columns', inplace=True)

    columnsTitles=['COUNT_ACTIVITIES', 'SEX', 'BIRTHPLACE', 'INSTITUTEID', 'ISOBCHAGA',
           'MARTIALSTATUSID', 'PUBLICATIONS', 'CONFERENCE', 'STUDACTIVE',
           'CREATICEACTIVE', 'SOCIALACTIVE', 'MEDALE', 'OLIMPIADE', 'TYPEOFSCHOOL',
           'COUNT_METTINGS', 'TIME_AUDIO_MINUTES',
           'TIME_VIDEO_MINUTES', 'SHARE_SCREEN_MINUTES', 'TET_A_TET_CALLS',
           'MS_MESSAGES', 'BALLSTOTAL']
    df=df.reindex(columns=columnsTitles)

    df.to_csv('Data.csv', index=False)
