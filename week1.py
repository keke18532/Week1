import pandas as pd
import numpy as np
def func(data):
    if (type(data) == float): return data
    result = np.array([])
    for string in data.split(" "):
        if (len(result) == 0 or result[-1] != string[0]):
            result = np.append(result, string[0])
    if (result.size == 1): return result[0]
    return result[result.argsort()[0]]

df=pd.read_csv('C:/Users/keke1/Desktop/Homework/Introduction to Data Science/Week1/train.csv')
df = df.drop(["Name", "Ticket", "PassengerId", "Parch", "SibSp"], axis=1)
df['Deck']=df["Cabin"].map(lambda x: type(x)!=float and len(x.split(" ") or x))
df["Cabin"] = df["Cabin"].map(func).astype('category').cat.codes
df = df.drop(["Cabin"], axis=1)
df["Sex"] = df["Sex"].astype('category').cat.codes
df["Embarked"] = df["Embarked"].astype('category').cat.codes
df["Deck"] = df["Deck"].fillna(df["Deck"].mode())
df["Survived"] = df["Survived"].fillna(df["Survived"].mode())
df["Pclass"] = df["Pclass"].fillna(df["Pclass"].mode())
df["Age"] = df["Age"].fillna(int(np.ceil(df["Age"].mean())))
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df.to_csv("./result.csv")
df.to_json("./result.json")