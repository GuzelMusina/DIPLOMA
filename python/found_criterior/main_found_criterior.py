import pandas as pd

from python.helpers.Reader import Reader
from python.helpers.Saver import Saver


# from python.found_criterior.Refactor import Refactor

import python.found_criterior.methods_for_criterior.FoundCriterior as foundCriterior

from python.found_criterior.methods_for_criterior.FeautureSelector import FeatureSelector
import python.found_criterior.methods_for_criterior.T_SNE as tsne


reader = Reader()
saver = Saver()

if __name__ == '__main__':
    # df = reader.readCSV('Data.csv')
    # df.drop(['GROUP_NUMBER'], axis='columns', inplace=True)
    # df.drop(['STUDENTID', 'FI', 'FIO'], axis='columns', inplace=True)
    # df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
    # df["BALLSTOTAL"] = df["BALLSTOTAL"].astype(int)
    # df["BALLSTOTAL"] = pd.to_numeric(df["BALLSTOTAL"], downcast='integer')
    # saver.saveToCSV(df, 'Data.csv')
    # refactor = Refactor()

    # X_embedded = tsne.fit(df)
    # print(X_embedded)

    # df = reader.readCSV('Data_with_class.csv')
    # foundCriterior.algorithmFoundCriterio(df, 0.8)

    # df1 = reader.readCSV('Success_data.csv')
    # print(len(df1[df1['SUCCESS']=='success'])/len(df1))
    # print(len(df1[df1['SUCCESS'] == 'partly success']) / len(df1))

    # y_ = [0 for x in range(len(df))]
    # for i in range(len(df)):
    #     if df.loc[i, 'BALLSTOTAL'] < 56:
    #         y_[i] = 0
    #     elif df.loc[i, 'BALLSTOTAL'] >= 56 and df.loc[i, 'BALLSTOTAL'] < 71:
    #         y_[i] = 1
    #     elif df.loc[i, 'BALLSTOTAL'] >= 71 and df.loc[i, 'BALLSTOTAL'] < 86:
    #         y_[i] = 2
    #     elif df.loc[i, 'BALLSTOTAL'] >= 86:
    #         y_[i] = 3
    # df.insert(21, 'CLASS', y_, True)
    # df.to_csv('Data_with_class.csv', index=False)
    foundCriterior










