import pandas as pd

from python.helpers.Reader import Reader
from python.helpers.Saver import Saver

reader = Reader()
saver = Saver()

if __name__ == '__main__':
    data = reader.readCSV('Data.csv')
    # data.drop(['GROUP_NUMBER'], axis='columns', inplace=True)
    data.drop(['FI', 'FIO'], axis='columns', inplace=True)
    saver.saveToCSV(data, 'Data.csv')
