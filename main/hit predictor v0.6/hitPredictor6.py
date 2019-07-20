#import os
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics, preprocessing
from scipy import stats
#from sklearn.feature_selection import VarianceThreshold

data = np.loadtxt('newSongfeat1.txt', delimiter=',',usecols=range(18))

#Removing Outliers
'''z = np.abs(stats.zscore(data))
data = data[(z < 3).all(axis=1)]'''



X, y = data[:, :17], data[:, 17]

print("Shape of X", X.shape)
print("Shape of y", y.shape)

X = preprocessing.scale(X)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=1)

model = MLPClassifier(solver='lbfgs',alpha=1e-1,hidden_layer_sizes=(10,2), random_state=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


y_pred = y_pred.reshape(y_pred.shape[0],-1)
y_test = y_test.reshape(y_test.shape[0],-1)

print("Shape of y_pred ", y_pred.shape)
print("Shape of y_test ", y_test.shape)


print("Accuracy: ", float(model.score(X_test, y_test))*100)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix: \n", cnf_matrix)