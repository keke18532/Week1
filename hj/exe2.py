import pandas as pd
import numpy as np
import json
import re
#from nltk.stem.porter import *
#from nltk.stem.snowball import SnowballStemmer
import sqlite3

json_str = open('../Automotive_5.json', 'rb').readlines()
stop = open("../stop-word-list.csv", 'rb').read()
#decode
json_str = [obj.decode("utf-8") for obj in json_str]
stop = stop.decode("utf-8")
#formalize
json_str = "["+",".join(json_str)+"]"
stop = np.array(stop.split(", "))
df = pd.read_json(json_str)

df["reviewText"] = df["reviewText"].map(lambda x:x.lower()).map(lambda x:re.sub(r'[^\w\s]','',x))

df["reviewText"] = df["reviewText"].map(lambda x: [word.strip() for word in x.split(" ") if word not in stop and len(word.strip())>0])

#stemmer = PorterStemmer()
stemmer = SnowballStemmer("english")
df["reviewText"] = df["reviewText"].map(lambda x: [stemmer.stem(word) for word in x])

df[df["overall"]>=4].to_csv("pos.txt")
df[df["overall"]<=2].to_csv("neg.txt")