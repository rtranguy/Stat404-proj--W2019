"""This is my code for homework five"""
import os
import numpy as np
import pandas as pd
from joblib import dump
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
os.chdir("C:\\Users\\Richard's Dell\\Documents\\Stats-404-W19-Statistical-Computing")
FILENAME = "StudentsPerformance1.csv"
DF = pd.read_csv(filepath_or_buffer=FILENAME, encoding='latin-1')
DF.columns = ['gender', 'race', 'degree', 'lunch', 'prep', 'math', 'reading', 'writing']
def total_score(math_score, reading, writing):
    """Function to computer total score"""
    return math_score + reading + writing
def average(math_score, reading, writing):
    """Function to compute average of scores"""
    return (math_score+reading+writing) / 3
def standardized_mean_score(mathavg, readingavg, writingavg):
    """Function to computer standardized mean total"""
    return mathavg+readingavg+writingavg
def standardized_std_score(mathstd, readingstd, writingstd):
    """Function to compute standardized standard deviation total"""
    return mathstd+readingstd+writingstd
MATHAVG = DF.loc[:, "math"].mean()
READINGAVG = DF.loc[:, "reading"].mean()
WRITINGAVG = DF.loc[:, "writing"].mean()
MATHSTD = DF.loc[:, "math"].std()
READINGSTD = DF.loc[:, "reading"].std()
WRITINGSTD = DF.loc[:, "writing"].std()
DF['pass'] = np.where(total_score(DF['math'], DF['reading'], DF['writing']) >=
                      standardized_mean_score(MATHAVG, READINGAVG, WRITINGAVG)
                      - standardized_std_score(MATHSTD, READINGSTD, WRITINGSTD), '1', '0')

INPUT = ['gender', 'race', 'degree', 'lunch', 'prep']
OUTPUT = ['pass']
X = pd.get_dummies(DF[INPUT])
Y = np.array(DF[OUTPUT]).ravel()
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, Y, test_size=0.30, random_state=1)
LB = preprocessing.LabelBinarizer()
LB.fit(Y)
Y_TRAINLB = LB.transform(Y_TRAIN)
Y_TESTLB = LB.transform(Y_TEST)
CLF = LogisticRegression(random_state=0, solver='lbfgs',
                         fit_intercept=False, multi_class='multinomial')
CLF.fit(X_TRAIN, Y_TRAIN)
Y_PROB = CLF.predict_proba(X_TEST)
Y_PRED = [x[1] for x in Y_PROB]
LOGREG = pd.DataFrame({'Features':X.columns.tolist(), 'Coefficient':CLF.coef_[0]})
LOGREG['odds'] = np.exp(LOGREG['Coefficient'])
LOGREG = LOGREG.sort_values(by=['odds'], ascending=False)
LOGREG = LOGREG.sort_values(by=['Features'], ascending=False)
dump(LOGREG, 'LR.joblib')
