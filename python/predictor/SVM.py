from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import metrics

def SVM(X_train, X_test, y_train, y_test):

    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train.ravel())
    expected = y_test.ravel()
    predicted = svclassifier.predict(X_test)

    acc = accuracy_score(expected, predicted)


    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    return acc