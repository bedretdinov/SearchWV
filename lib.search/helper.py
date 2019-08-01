from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re
import pymorphy2
import numpy as np
import pandas as pd

morph = pymorphy2.MorphAnalyzer()






class mean_vectorizer(object):

    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = len(next(iter(self.word2vec.values())))

    def fit(self, X):
        return self

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])


class TextFeatures:

    def tokenizer(x):
        x = x.lower()

        x = x.replace('заплатите', '')
        x = x.replace('вместо', '')
        x = x.replace('скидка', '')
        x = x.replace('скидка', '')

        x = re.sub(r'!', '', x)
        x = re.sub(r'<[^>]+>', '', x)
        x = re.sub(r'[0-9]+%', '', x)
        x = re.sub(r'[0-9]+', '', x)
        x = re.sub(r'«|»', '', x)
        x = re.sub(r'—|\)|\(|:|-|’', '', x)
        x = re.sub(r'&nbsp;', ' ', x)
        x = list(filter(lambda x: x != '', re.split(r'\s|,|\.', x)))

        ru_stop = stopwords.words('russian')

        #     if(isinstance(tf_dataframe, (pd.core.frame.DataFrame))):
        #         if(tf_dataframe.empty!=True):
        #             term_th = tf_dataframe[tf_dataframe.weight<0.00001].term.values
        #             ru_stop.extend(term_th)

        x = list(set(x) - set(ru_stop))

        return [morph.parse(w)[0].normal_form for w in x]

    def Tfidf_Vectorize(lemmas_name):
        vect = TfidfVectorizer(tokenizer=TextFeatures.tokenizer)
        vect_transform = vect.fit_transform(lemmas_name)

        vect_score = np.asarray(vect_transform.mean(axis=0)).ravel().tolist()
        vect_array = pd.DataFrame({'term': vect.get_feature_names(), 'weight': vect_score})
        vect_array.sort_values(by='weight', ascending=False, inplace=True)

        return vect_array
