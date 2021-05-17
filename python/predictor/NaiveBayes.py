from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

def NaiveBayes(X_train, X_test, y_train, y_test):
    model = GaussianNB()
    model.fit(X_train, y_train.ravel())
    expected = y_train.ravel()
    predicted = model.predict(X_train)

    acc = accuracy_score(expected, predicted)

    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    return acc