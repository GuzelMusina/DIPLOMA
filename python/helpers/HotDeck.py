import timeit
import numpy as np
import math
from collections import Counter
import pandas as pd

fileName = pd.read_csv('New_data.csv')
createOutputFile = True
calculateMSE = True

imported = []
row = 0
missing = []
importedNM = []
importedNM_index = []
tagList = []
tagListNM = []
strings = {}

col = len(imported[0]) - 1

for i in range(row):
    tagList.append(imported[i][col])
    del (imported[i][-1])
    missingFlag = False
    for j in range(col):
        if imported[i][j] != '':
            v = imported[i][j]
        else:
            missing.append([i, j])
            missingFlag = True
    if not missingFlag:
        importedNM_index.append(i)
        importedNM.append(imported[i])
        tagListNM.append(tagList[i])
tags = Counter(tagList).most_common()
miss = len(missing)
dataSet = np.array(imported)
dataSetNM = np.array(importedNM)


def HotDeck():
    kHD = 20
    for idx, v in enumerate(missing):
        i, j = v
        euclidean = []
        euclideanTotal = 0
        for r in range(len(importedNM)):
            for c in range(col):
                if c != j:
                    euclideanTotal += (imported[i][c] - importedNM[r][
                        c]) ** 2
            e = math.sqrt(euclideanTotal)
            euclidean.append(
                [e, importedNM_index[r]])
        sorted(euclidean, key=lambda l: l[0], reverse=True)
        lst = [imported[euclidean[r][1]][j] for r in range(kHD)]
        imported[i][j] = Counter(lst).most_common(1)[0][0]
