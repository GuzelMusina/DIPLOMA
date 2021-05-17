import pandas as pd
from sklearn import tree

# Import the necessary modules and libraries
import numpy as np

import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

from python.predictor.DesicionTree import DecisonTreeRegressor
from python.predictor.SVM import SVM
from python.predictor.NaiveBayes import NaiveBayes
from python.predictor.NN import NN

# Split the data into training and testing set
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    df = pd.read_csv('../found_criterior/New_data.csv')
    TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    Predictors = ['COUNT_ACTIVITIES', 'SEX', 'BIRTHPLACE', 'ISOBCHAGA', 'MARTIALSTATUSID',
                  'PUBLICATIONS', 'CONFERENCE', 'STUDACTIVE', 'CREATICEACTIVE',
                  'SOCIALACTIVE', 'MEDALE', 'OLIMPIADE', 'TYPEOFSCHOOL', 'COUNT_METTINGS',
                  'TIME_AUDIO_MINUTES', 'TIME_VIDEO_MINUTES', 'SHARE_SCREEN_MINUTES',
                  'TET_A_TET_CALLS', 'MS_MESSAGES', 'BALLSTOTAL', 'CLASS']

    X = df[Predictors].values
    y = df[TargetVariable].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # ACC_DECISION_TREE = DecisonTreeRegressor(X_train, X_test, y_train, y_test)
    # print(ACC_DECISION_TREE)
    #
    # ACC_SVM = SVM(X_train, X_test, y_train, y_test)
    # print(ACC_SVM)
    #
    # ACC_NAIVE_BAYES = NaiveBayes(X_train, X_test, y_train, y_test)
    # print(ACC_NAIVE_BAYES)

    ACC_NN = NN(df)
    print(ACC_NN)

