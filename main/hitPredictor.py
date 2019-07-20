import os
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, preprocessing
from scipy import stats

data = np.loadtxt('songdatabase1.txt', delimiter='\t')

#Removing Outliers
z = np.abs(stats.zscore(data))
data = data[(z < 3).all(axis=1)]



X, y = data[:, :16], data[:, 16]

print("Shape of X", X.shape)
print("Shape of y", y.shape)

X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=1)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


y_pred = y_pred.reshape(y_pred.shape[0],-1)
y_test = y_test.reshape(y_test.shape[0],-1)

print("Shape of y_pred ", y_pred.shape)
print("Shape of y_test ", y_test.shape)


print("Accuracy: ", float(model.score(X_test, y_test))*100)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix: \n", cnf_matrix)