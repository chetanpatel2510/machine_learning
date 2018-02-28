import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
balance_data = pd.read_csv('C:/Users/Chetan/Desktop/mpg1.csv')
X = balance_data.values[:, 1:7]
Y = balance_data.values[:,0]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

#clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
 #                              max_depth=6, min_samples_leaf=7)

clf_gini = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=10, min_samples_leaf=5, max_features=5)

print (clf_gini)
model = clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)
print (y_pred)
print ("Accuracy is ", accuracy_score(y_test,y_pred)*100);



with open("C:/Users/Chetan/Desktop/decision_tree_classifier.txt", "w") as f:
    f = tree.export_graphviz(clf_gini, out_file=f)
    