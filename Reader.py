import pandas as pd

class Reader(object):

    def readCSV(self, path):
        dataset = pd.read_csv(path)
        return dataset

    def readCSVWithSeparator(self, path):
        dataset = pd.read_csv(path, sep=';')
        return dataset