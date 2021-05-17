# importing the libraries
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np

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


def NN(df):

    temp=[]
    for i in range(len(df)):
        if df.loc[i,'CLASS'] == 0:
            temp.append(0)
        elif df.loc[i,'CLASS'] == 1:
            temp.append(1)
        elif df.loc[i,'CLASS'] == 2 or df.loc[i,'CLASS'] == 3:
            temp.append(2)

    df['CLASS_CHECK'] = temp

    TargetVariable = ['SUCCESS_METRICS_NUMBERS']
    Predictors = ['COUNT_ACTIVITIES', 'SEX', 'BIRTHPLACE', 'ISOBCHAGA', 'MARTIALSTATUSID',
                  'PUBLICATIONS', 'CONFERENCE', 'STUDACTIVE', 'CREATICEACTIVE',
                  'SOCIALACTIVE', 'MEDALE', 'OLIMPIADE', 'TYPEOFSCHOOL', 'COUNT_METTINGS',
                  'TIME_AUDIO_MINUTES', 'TIME_VIDEO_MINUTES', 'SHARE_SCREEN_MINUTES',
                  'TET_A_TET_CALLS', 'MS_MESSAGES', 'BALLSTOTAL', 'CLASS']

    X = df[Predictors].values
    y = df[TargetVariable].values

    ### Sandardization of data ###
    from sklearn.preprocessing import StandardScaler

    PredictorScaler = StandardScaler()
    TargetVarScaler = StandardScaler()

    # Storing the fit object for later reference
    PredictorScalerFit = PredictorScaler.fit(X)
    TargetVarScalerFit = TargetVarScaler.fit(y)

    # Generating the standardized values of X and y
    X = PredictorScalerFit.transform(X)
    y = TargetVarScalerFit.transform(y)

    # Split the data into training and testing set
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



    # create ANN model
    model = Sequential()

    # Defining the Input layer and FIRST hidden layer, both are same!
    model.add(Dense(units=5, input_dim=21, kernel_initializer='normal', activation='relu'))

    # Defining the Second layer of the model
    # after the first layer we don't have to specify input_dim as keras configure it automatically
    model.add(Dense(units=5, kernel_initializer='normal', activation='tanh'))

    # The output neuron is a single fully connected node
    # Since we will be predicting a single number
    model.add(Dense(1, kernel_initializer='normal'))

    # Compiling the model
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Fitting the ANN to the Training set
    model.fit(X_train, y_train ,batch_size = 20, epochs = 150, verbose=1)
######################################################
# Calling the function
#     ResultsData = FunctionFindBestParams(X_train, y_train, X_test, y_test)

    # Fitting the ANN to the Training set
    model.fit(X_train, y_train, batch_size=20, epochs=100, verbose=0)

    # Generating Predictions on testing data
    Predictions = model.predict(X_test)

    # Scaling the predicted Price data back to original price scale
    Predictions = TargetVarScalerFit.inverse_transform(Predictions)

    # Scaling the y_test Price data back to original price scale
    y_test_orig = TargetVarScalerFit.inverse_transform(y_test)

    # Scaling the test data back to original scale
    Test_Data = PredictorScalerFit.inverse_transform(X_test)

    TestingData = pd.DataFrame(data=Test_Data, columns=Predictors)
    TestingData['SUCCESS_METRICS_NUMBERS'] = y_test_orig

    for i in range(len(Predictions)):
        Predictions[i] = int(Predictions[i])

    TestingData['SUCCESS_METRICS_NUMBERS_PREDICT'] = Predictions


    # Computing the absolute percent error
    APE = 100 * (abs(TestingData['SUCCESS_METRICS_NUMBERS'] - TestingData['SUCCESS_METRICS_NUMBERS_PREDICT']) /
                 TestingData['SUCCESS_METRICS_NUMBERS'])
    TestingData['APE'] = APE

    acc = 100 - np.mean(APE)
    print('The Accuracy of ANN model is:', acc)

    return acc




