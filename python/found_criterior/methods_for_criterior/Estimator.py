from scipy.stats import entropy
from pandas import pd
class Estimator(object):
    def __init__(self, result1, result2, result3):
        self.result1 = result1
        self.result2 = result2
        self.result3 = result3
        self.data=pd.read_csv('Data.csv')


    def entropy(self):
        e1 = entropy(self.result1['CLUSTER'],self.data['CLASS'])
        e2 = entropy(self.result2['CLUSTER'], self.data['CLASS'])
        e3 = entropy(self.result3['CLUSTER'], self.data['CLASS'])

        return min(e1,e2,e3)

    def hubertGStatistic(self):
        n = len(self.data)
        M = n*(n-1)/2


