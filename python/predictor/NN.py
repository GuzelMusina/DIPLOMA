# importing the libraries
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score

# To remove the scientific notation from numpy arrays
np.set_printoptions(suppress=True)

# Defining a function to find the best parameters for ANN
def FunctionFindBestParams(X_train, y_train, X_test, y_test):
    # Defining the list of hyper parameters to try
    batch_size_list = [5, 10, 15, 20]
    epoch_list = [5, 10, 50, 100]

    import pandas as pd
    SearchResultsData = pd.DataFrame(columns=['TrialNumber', 'Parameters', 'Accuracy'])

    # initializing the trials
    TrialNumber = 0
    for batch_size_trial in batch_size_list:
        for epochs_trial in epoch_list:
            TrialNumber += 1
            # create ANN model
            model = Sequential()
            # Defining the first layer of the model
            model.add(Dense(units=5, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu'))

            # Defining the Second layer of the model
            model.add(Dense(units=5, kernel_initializer='normal', activation='relu'))

            # The output neuron is a single fully connected node
            # Since we will be predicting a single number
            model.add(Dense(1, kernel_initializer='normal'))

            # Compiling the model
            model.compile(loss='mean_squared_error', optimizer='adam')

            # Fitting the ANN to the Training set
            model.fit(X_train, y_train, batch_size=batch_size_trial, epochs=epochs_trial, verbose=0)

            MAPE = np.mean(100 * (np.abs(y_test - model.predict(X_test)) / y_test))

            # printing the results of the current iteration
            print(TrialNumber, 'Parameters:', 'batch_size:', batch_size_trial, '-', 'epochs:', epochs_trial,
                  'Accuracy:', 100 - MAPE)

            SearchResultsData = SearchResultsData.append(
                pd.DataFrame(data=[[TrialNumber, str(batch_size_trial) + '-' + str(epochs_trial), 100 - MAPE]],
                             columns=['TrialNumber', 'Parameters', 'Accuracy']))
    return (SearchResultsData)


def NN(X_train, X_test, y_train, y_test):

    # temp=[]
    # for i in range(len(df)):
    #     if df.loc[i,'CLASS'] == 0:
    #         temp.append(0)
    #     elif df.loc[i,'CLASS'] == 1:
    #         temp.append(1)
    #     elif df.loc[i,'CLASS'] == 2 or df.loc[i,'CLASS'] == 3:
    #         temp.append(2)
    #
    # df['CLASS_CHECK'] = temp
    #
    # TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    # Predictors = ['COUNT_ACTIVITIES', 'SEX', 'BIRTHPLACE', 'ISOBCHAGA', 'MARTIALSTATUSID',
    #               'PUBLICATIONS', 'CONFERENCE', 'STUDACTIVE', 'CREATICEACTIVE',
    #               'SOCIALACTIVE', 'MEDALE', 'OLIMPIADE', 'TYPEOFSCHOOL', 'COUNT_METTINGS',
    #               'TIME_AUDIO_MINUTES', 'TIME_VIDEO_MINUTES', 'SHARE_SCREEN_MINUTES',
    #               'TET_A_TET_CALLS', 'MS_MESSAGES', 'BALLSTOTAL', 'CLASS']

    INPUT = 9
    UNITS = 36
    # importing the libraries
    from keras.models import Sequential
    from keras.layers import Dense

    # create ANN model
    model = Sequential()

    # Defining the Input layer and FIRST hidden layer, both are same!
    model.add(Dense(units=36, input_dim=INPUT, kernel_initializer='normal', activation='linear'))

    # Defining the Second layer of the model
    # after the first layer we don't have to specify input_dim as keras configure it automatically
    model.add(Dense(units=72, kernel_initializer='normal', activation='linear'))
    model.add(Dense(units=72, kernel_initializer='normal', activation='linear'))
        # The output neuron is a single fully connected node
    # Since we will be predicting a single number
    model.add(Dense(1, kernel_initializer='normal'))

    # Compile the network :
    model.compile(loss='mean_absolute_error', optimizer='RMSProp', metrics=['mean_absolute_error'])
    model.summary()

    # Compiling the model
    model.compile(loss='mean_absolute_error', optimizer='RMSProp')

    # Fitting the ANN to the Training set
    model.fit(X_train, y_train, batch_size=20, epochs=50)

    predict = model.predict(X_test)
    predict = abs(predict.ravel())
    expect = y_test.ravel()
    for i in range(len(predict)):
        predict[i] = int(round(predict[i]))
    expect = y_test.ravel()

    mae = metrics.mean_absolute_error(expect, predict)
    mse = metrics.mean_squared_error(expect, predict)
    rmse = np.sqrt(mse)  # or mse**(0.5)
    r2 = metrics.r2_score(expect, predict)

    print("Results of sklearn.metrics:")
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R-Squared:", r2)

    print(metrics.classification_report(expect, predict))
    print(metrics.confusion_matrix(expect, predict))

    # return accuracy_score(expect, predict)




