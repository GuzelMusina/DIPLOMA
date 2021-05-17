from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import metrics

def DecisonTreeRegressor(X_train, X_test, y_train, y_test):


    # Fit regression model
    # regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    # regr_1.fit(X_train, y_train)
    regr_2.fit(X_train, y_train)

    predicted = np.asarray(regr_2.predict(X_test))
    expected=y_test

    for i in range(len(predicted)):
        predicted[i] = int(predicted[i])

    expected = expected.astype("float")
    predicted = predicted.astype("float")

    acc = accuracy_score(expected.ravel(), predicted)

    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    return acc
