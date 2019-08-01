import pickle
import warnings
import json
import os
import sys
from helper import  TextFeatures,   mean_vectorizer
from annoy import AnnoyIndex

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

warnings.filterwarnings("ignore")

findText = sys.argv[1]

f = 300
u = AnnoyIndex(f)
u.load('./models/index.ann') # super fast, will just mmap the file

with open('./models/mean_vectorizer.pickle', 'rb') as handle:
    wv = pickle.load(handle)


words_t = TextFeatures.tokenizer(findText)

nns = u.get_nns_by_vector(wv.transform([words_t])[0] ,3)


print(json.dumps(nns))
