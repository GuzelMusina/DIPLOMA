import pandas as pd

class Merger(object):

    def merge(self, dataset1, dataset2, param):
        # merge dataset1 and dataset2 by param
        data = pd.merge(dataset1, dataset2, on=param)
        return data