from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report , confusion_matrix
from multiprocessing import context
from io import StringIO
import multiprocessing

def diabetes(request):
    return render(request , "diabetes.html")

def register(request):
    return render(request, "register.html")
    

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def predict(request):
    return render(request, "predict.html")

def outcome(request):
    df = pd.read_csv(r"C:\Users\visha\OneDrive\Documents\Machine Learning\diabetes.csv")

    X = df.drop("Outcome" , axis=1)
    Y = df['Outcome']
    X_train , X_test, Y_train, Y_test = train_test_split(X,Y , test_size=0.2, random_state=0)

    logmodel = LogisticRegression()
    logmodel.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = logmodel.predict([[val1,val2,val3, val4, val5, val6, val7, val8]])
    #1 is positive
    #0 is negative

    result1=""
    if pred==[1]:
        result1="1: You are Diabetic"

    else:
        result1="0: You are not Diabetic"
    return render(request, "predict.html", {"result2":result1})
