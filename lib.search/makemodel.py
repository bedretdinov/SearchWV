from databas import DataBase as DB
import json
from sklearn.neighbors import NearestNeighbors
from helper import  TextFeatures,   mean_vectorizer
import pickle
import warnings
import sys
import os
from annoy import AnnoyIndex


warnings.filterwarnings("ignore")

apiquery = sys.argv[1]

with open('./models/mean_vectorizer.pickle', 'rb') as handle:
    wv = pickle.load(handle)

deals               = DB.Slave(apiquery)
deals.columns       = ['ID','TEXT']
deals['TEXT_AR']    = deals.TEXT.map(TextFeatures.tokenizer)


data_mean=wv.transform(deals.TEXT_AR.values)

f = 300
t = AnnoyIndex(f)  # Length of item vector that will be indexed
for i,v in enumerate(data_mean):
    t.add_item(deals.ID.values[i], v)

t.build(10) # 10 trees
t.save('./models/index.ann')

print(json.dumps({'successfully':'true'}))