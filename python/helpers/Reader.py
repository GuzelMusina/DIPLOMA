import pandas as pd

class Reader(object):

    def readCSV(self, path):
        dataset = pd.read_csv(path)
        return dataset