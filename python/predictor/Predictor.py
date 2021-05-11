import pandas as pd
from sklearn import tree

# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error


if __name__ == '__main__':
    df = pd.read_csv('../found_criterior/New_data.csv')
    X_train = df.loc[:2900,['BALLSTOTAL']]
    y_train = df.loc[:2900,'SUCCESS_METRICS_NUMBERS']

    # Fit regression model
    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X_train, y_train)
    regr_2.fit(X_train, y_train)

    X_test = df.loc[2901:,['BALLSTOTAL']]
    y_1 = regr_1.predict(X_test)
    y_2 = regr_2.predict(X_test)

    y_actual = df.loc[2901:, 'SUCCESS_METRICS_NUMBERS']
    y_expected = []
    for i in range(len(y_2)):
        y_expected.append(int(round(y_2[i])))

    print(mean_absolute_error(y_actual.values, y_expected))