import pandas as pd

from python.helpers.Reader import Reader
from python.helpers.Saver import Saver

reader = Reader()
saver = Saver()

if __name__ == '__main__':
    df = reader.readCSV('Data.csv')
    df.drop(['GROUP_NUMBER'], axis='columns', inplace=True)
    df.drop(['STUDENTID', 'FI', 'FIO'], axis='columns', inplace=True)
    df["BALLSTOTAL"] = df["BALLSTOTAL"].astype(int)
    # df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
    saver.saveToCSV(df, 'Data1.csv')

    names = df.columns
    mess_arr = []
    for j in range(len(df)):
        summ = df['CHANNEL_MESSAGE'][j] + df['PUBLISHED_MESSAGES'][j] + df['CHAT_MESSAGES'][j] + df['URGENT_MESSAGES'][
            j]
        mess_arr.append(summ)
    df.insert(len(names), 'MS_MESSAGES', mess_arr, True)

    df.drop(['KINDTRAINING', 'TYPETRAINING', 'CATEGORYID',
             'QUALIFICATIONTYPE', 'STUDTYPE_ID', 'HOW_MUCH_METTINGS_WERE_ORGANIZE',
             'CHANNEL_MESSAGE', 'PUBLISHED_MESSAGES', 'CHAT_MESSAGES', 'URGENT_MESSAGES'
             ], axis='columns', inplace=True)










