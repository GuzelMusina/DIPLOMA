from scipy.stats import entropy
from pandas import pd
import math
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
        P=[]
        Q=[]
        for i in range(len(self.result1)):
            for j in range(len(self.result2)):
                P[i,j] = abs(self.result1[i]-self.result2[i])
                if self.result1.target == self.result2.target:
                    Q[i,j]=1
                else:
                    Q[i,j]=0
        G = 1/M(P*Q)
        return G

    def foulksaMellow(self):
        TP = 0
        FP = 0
        FN = 0

        for i in range(len(self.result1)):
            if self.result1[i] == self.result2[i] == 'O':
                TP += 1
            if self.result1[i] != 'O' and self.result2[i] == 'O':
                FP += 1
            if self.result1[i] == self.result2[i] == '/' or self.result1[i] == self.result2[i] == '*':
                TN += 1
            if self.result1[i] == 'O' and self.result2[i] != 'O':
                FN += 1
            if self.result1[i] == '-':  # just ignore the '-' and move on to the next
                i += 1
        FM = math.sqrt(TP/(TP+FP)*TP/(TP+FN))

        return FM
