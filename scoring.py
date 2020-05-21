"""
This script loads my logistic regression and prompts the 5 factors to calculate Pass / No Pass
"""
from joblib import load
LR = load('LR.joblib')
RACE_INPUT = input("Race | Input A-E (case sensitive) : ")
RACEA = RACEB = RACEC = RACED = RACEE = 0
if RACE_INPUT == "A":
    RACEA = 1
if RACE_INPUT == "B":
    RACEB = 1
if RACE_INPUT == "C":
    RACEC = 1
if RACE_INPUT == "D":
    RACED = 1
if RACE_INPUT == "E":
    RACEE = 1
RACE_OUTPUT = LR.iloc[0][1]*RACEE + LR.iloc[1][1]*RACED + LR.iloc[2][1]*RACEC + LR.iloc[3][1]*RACEB + LR.iloc[4][1]*RACEA
GENDER = input("Gender | M = Male | F = Female : ")
GENDERM = GENDERF = 0
if GENDER == 'M':
    GENDERM = 1
    GENDERF = 0
if GENDER == 'F':
    GENDERM = 0
    GENDERF = 1
GENDER_OUTPUT = LR.iloc[9][1]*GENDERM + LR.iloc[10][1]*GENDERF
PREP = input("Preperatory Course | 1=Yes | 0=No : ")
PREP0 = PREP1 = 0
if PREP == '1':
    PREP1 = 1
    PREP0 = 0
if PREP == '0':
    PREP1 = 0
    PREP0 = 1
PREP_OUTPUT = LR.iloc[5][1]*PREP0+LR.iloc[6][1]*PREP1
LUNCH = input("Lunch | 1 = Paid | 0 = Free/Reduced : ")
LUNCH0 = LUNCH1 = 0
if LUNCH == '1':
    LUNCH1 = 1
if LUNCH == '0':
    LUNCH1 = 0
    LUNCH0 = 1
LUNCH_OUTPUT = LR.iloc[7][1]*LUNCH1 + LR.iloc[8][1]*LUNCH0
PARENT = input("Parent Education Level | 1 = Some High School, 2 = High School, 3 = Some College, 4 = Associate's Degree, 5 = Bachelor's Degree, 6 = Master's Degree : ")
PARENTSHS = PARENTSC = PARENTMD = PARENTHS = PARENTB = PARENTA = 0
if PARENT == "1":
    PARENTSHS = 1
if PARENT == "2":
    PARENTHS = 1
if PARENT == "3":
    PARENTSC = 1
if PARENT == "4":
    PARENTA = 1
if PARENT == "5":
    PARENTB = 1
if PARENT == "6":
    PARENTMD = 1 
PARENT_OUTPUT = LR.iloc[11][1]*PARENTSHS+LR.iloc[12][1]*PARENTSC+LR.iloc[13][1]*PARENTMD + LR.iloc[14][1]*PARENTHS + LR.iloc[15][1]*PARENTB + LR.iloc[16][1]*PARENTA
LOGREG = RACE_OUTPUT + PREP_OUTPUT + LUNCH_OUTPUT + GENDER_OUTPUT + PARENT_OUTPUT
if ((RACE_OUTPUT == 0) or (PREP_OUTPUT == 0) or (LUNCH_OUTPUT == 0) or (GENDER_OUTPUT == 0) or (PARENT_OUTPUT == 0)):
    print("Wrong input, try again")
elif LOGREG >= .5:
    print("PASS! :)")
elif LOGREG < .5:
    print("FAIL :(")
input("Press any key to exit")
