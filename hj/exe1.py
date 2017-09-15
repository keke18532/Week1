import pandas as pd
import numpy as np
import json
import re
#from nltk.stem.porter import *
#from nltk.stem.snowball import SnowballStemmer
import sqlite3

#cd e:/document/ids/data sets
#1
train = pd.read_csv("../train.csv")
train.columns

df = train.drop("Name",axis=1).drop("Ticket",axis=1)

df.columns

def func(data):
    if(type(data)==float): return data
    result = ""
    for string in data.split(" "):
        if(len(result)==0 or result[-1]!=string[0]):
            result += string[0]
    return result
df["Deck"] = df["Cabin"].map(func)
df["Deck"] = df["Deck"].astype('category').cat.codes
df = df.drop("Cabin",axis=1)

df["Sex"] = df["Sex"].astype('category').cat.codes
df["Embarked"] = df["Embarked"].astype('category').cat.codes

df["Survived"] = df["Survived"].fillna(df["Survived"].mode())
df["Pclass"] = df["Pclass"].fillna(df["Pclass"].mode())
df["Sex"] = df["Sex"].fillna(df["Sex"].mode())
df["Age"] = df["Age"].fillna(int(np.ceil(df["Age"].mean()))).map(lambda x:int(np.ceil(x)))
df["SibSp"] = df["SibSp"].fillna(df["SibSp"].mode())
df["Parch"] = df["Parch"].fillna(df["Parch"].mode())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode())
deckmdoe = int(df["Deck"].map(lambda x:x==-1 and np.nan or x).mode())
df["Deck"] = df["Deck"].map(lambda x:x==-1 and deckmdoe or x)

df.to_csv("./processed.csv",index=False)
df.to_json("./processed.json",orient="records",lines=True)
