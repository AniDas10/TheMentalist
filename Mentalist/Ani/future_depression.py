from sklearn import tree
from info_gain import info_gain
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation 
import csv

def help(features):
    col_names = ['Gender','self_employed','family_history','remote_work','work_interfere','treatment']
    # load dataset
    pima = pd.read_csv("surveyEncoded.csv", header=None, names=col_names)

    feature_cols = ['Gender','self_employed','family_history','remote_work','work_interfere']
    X = pima[feature_cols] # Features
    y = pima.treatment # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    prediction = clf.predict([features])
    # print(prediction)
    if(prediction[0]==1):
        return 1
    else:
        return 0

# Male = 1