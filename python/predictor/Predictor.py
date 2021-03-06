import pandas as pd
import streamlit as st

# Import the necessary modules and libraries
from python.predictor.DesicionTree import DecisonTreeRegressor
from python.predictor.NN import NN

# Split the data into training and testing set
from sklearn.model_selection import train_test_split

from python.predictor.NaiveBayes import NaiveBayes
from python.predictor.SVM import SVM

if __name__ == '__main__':
    st.write("HIII")
    df = pd.read_csv('../../data/New_data.csv')
    TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    Predictors = ['COUNT_ACTIVITIES', 'COUNT_METTINGS', 'SHARE_SCREEN_MINUTES', 'TIME_VIDEO_MINUTES',
                  'TIME_AUDIO_MINUTES', 'MS_MESSAGES', 'TET_A_TET_CALLS', 'TYPEOFSCHOOL',
                  'PUBLICATIONS']

    X = df[Predictors].values
    y = df[TargetVariable].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    ACC_DECISION_TREE = DecisonTreeRegressor(X_train, X_test, y_train, y_test)
    print(ACC_DECISION_TREE)

    ACC_SVM = SVM(X_train, X_test, y_train, y_test)
    print(ACC_SVM)

    ACC_NAIVE_BAYES = NaiveBayes(X_train, X_test, y_train, y_test)
    print(ACC_NAIVE_BAYES)

    ACC_NN = NN(X_train, X_test, y_train, y_test)
    # ACC_NN

    choose_best_model(ACC_DECISION_TREE, ACC_SVM, ACC_NAIVE_BAYES, ACC_NN)


def choose_best_model(ACC_DECISION_TREE, ACC_SVM, ACC_NAIVE_BAYES, ACC_NN):
    best = max(ACC_DECISION_TREE, ACC_SVM, ACC_NAIVE_BAYES, ACC_NN)
    if best == ACC_DECISION_TREE:
        return "Decision Tree"
    elif best == ACC_SVM:
        return "SVM"
    elif best == ACC_NAIVE_BAYES:
        return "NAIVE_BAYES"
    else:
        return "NN"
