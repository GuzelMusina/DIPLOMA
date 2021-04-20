import pandas as pd

from python.helpers.Reader import Reader
from python.helpers.Saver import Saver


from python.found_criterior.Refactor import Refactor

import python.found_criterior.methods_for_criterior.T_SNE as tsne

reader = Reader()
saver = Saver()

if __name__ == '__main__':
    df = reader.readCSV('Data.csv')
    # df.drop(['GROUP_NUMBER'], axis='columns', inplace=True)
    # df.drop(['STUDENTID', 'FI', 'FIO'], axis='columns', inplace=True)
    # df["BALLSTOTAL"] = df["BALLSTOTAL"].astype(int)
    # # df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
    # saver.saveToCSV(df, 'Data1.csv')
    refactor = Refactor()

    X_embedded = tsne.fit()











