# -*- coding: utf-8 -*-
"""BreastCancerPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eVUCzIDdTd-t57YiS7dL3lHCFEBbLf5F

STEP 1:IMPORT LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""STEP 2:IMPORT DATASET"""

data=pd.read_csv('breastCancer.csv')
X=data.iloc[:,:-1].values
Y=data.iloc[:,-1].values

"""STEP 3 SPLIT INTO TRAINING AND TESTING DATA SET"""

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

"""Feature Scaling"""

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_new=sc.fit_transform(X_train)
X_newtest=sc.fit_transform(X_test)

"""STEP 4:APPLY VARIOUS MODELS

4.1.a:LOGISTIC REGRESSION
"""

#applying the model
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_new,Y_train)

#predicting
lrY_pred=lr.predict(X_newtest)
lrY_pred

#confusion matrix and accuracy score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
lrcm=confusion_matrix(Y_test,lrY_pred)
lrac=accuracy_score(Y_test,lrY_pred)
print(lrcm,lrac)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print("For Logistic Regression")
print("precision:",precision_score(Y_test,lrY_pred))
print("Recall:",recall_score(Y_test,lrY_pred))

#visualisation of all logistic REgression
plt.plot(Y_test,color="red")
plt.plot(lrY_pred,color="black")
plt.title("Logistic Regression")

"""4.2 KNN"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_new,Y_train)
print("-----------------Predicting for test dataset -------------")
print(knn.predict(X_newtest))

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
kncm=confusion_matrix(Y_test,knn.predict(X_newtest))
knac=accuracy_score(Y_test,knn.predict(X_newtest))
print(kncm,"\n",knac)

print("For KNN")
print("precision:",precision_score(Y_test,knn.predict(X_newtest)))
print("Recall:",recall_score(Y_test,knn.predict(X_newtest)))

#visualisation for KNN
plt.plot(Y_test,color="red")
plt.plot(knn.predict(X_newtest),color="black")
plt.title("KNN of n=5")

"""4.C :SVM classifier"""

from sklearn.svm import SVC
svc=SVC()
svc.fit(X_new,Y_train)
print("-----------------Predicting for test dataset -------------")
print(svc.predict(X_newtest))

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
svccm=confusion_matrix(Y_test,svc.predict(X_newtest))
svcac=accuracy_score(Y_test,svc.predict(X_newtest))
print(svccm,"\n",svcac)

print("For SVM")
print("precision:",precision_score(Y_test,svc.predict(X_newtest)))
print("Recall:",recall_score(Y_test,svc.predict(X_newtest)))

#visualisation for SVM
plt.plot(Y_test,color="red")
plt.plot(svc.predict(X_newtest),color="black")
plt.title("SVM Classifier" )

"""4.D NAIVE BAYES IMPLEMENTATION"""

from sklearn.naive_bayes import GaussianNB
Nc=GaussianNB()
Nc.fit(X_new,Y_train)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
Nccm=confusion_matrix(Y_test,Nc.predict(X_newtest))
Ncac=accuracy_score(Y_test,Nc.predict(X_newtest))
print(Nccm,"\n",Ncac)

Nc.predict(X_newtest)

print("for Naive Bayes")
print("precision:",precision_score(Y_test,Nc.predict(X_newtest)))
print("Recall:",recall_score(Y_test,Nc.predict(X_newtest)))

#visualisation for Naive Bayes
plt.plot(Y_test,color="red")
plt.plot(Nc.predict(X_newtest),color="black")
plt.title("Naive Bayes Classifier" )

"""4.E ID3 CLASSIFIER IMPLEMENTATION"""

from sklearn.tree import DecisionTreeClassifier
DC=DecisionTreeClassifier()
k=DC.fit(X_new,Y_train)
DC.fit(X_new,Y_train)

from sklearn.metrics import confusion_matrix,accuracy_score
DCcm=confusion_matrix(Y_test,DC.predict(X_test))
DCam=accuracy_score(Y_test,DC.predict(X_test))
print(DCcm,"\n",DCam)

DC.predict(X_test)

#visualisation for Decision Tree Classifier
plt.plot(Y_test,color="red")
plt.plot(DC.predict(X_newtest),color="black")
plt.title("Decision Tree Classifier" )

#Decision tree plot
from sklearn.datasets import load_iris
from sklearn import tree
tree.plot_tree(k)

print("ID3 Classifier")
print("precision:",precision_score(Y_test,DC.predict(X_newtest)))
print("Recall:",recall_score(Y_test,DC.predict(X_newtest)))

#plot all accuracies in the form of the histogram
import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Logistic':lrac, 'KNN':knac, 'SVM':svcac,
        'Naive-Bayes':Ncac,'ID3':DCam}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values,width = 0.4)

plt.xlabel("Classifiers")
plt.ylabel("Accuracies")
plt.title("Accuracies of different Classifiers")
plt.show()

X_newest=data.iloc[5:6,:-1].values

X_newest

#logistic prediction
k1=lr.predict(X_newest)
k1