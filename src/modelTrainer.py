import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
# modelo versión 2
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline

nltk.download('stopwords')
import re
from unicodedata import normalize

from bs4 import BeautifulSoup

# Traemos los datos
df = pd.read_csv('https://gist.githubusercontent.com/rgonzalezt/7b21f9909a8b52436d1d7003e04208e1/raw/51efddfaf88a16ef336c426da529094799743c15/ejercicios_modelo_12_11.csv')

df = df[pd.notnull(df['tag'])]

# Limpieza de datos
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
STOPWORDS = set(stopwords.words('spanish'))


def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = BeautifulSoup(text, "lxml").text  # HTML decoding
    text = text.lower()  # lowercase text
    # text = REPLACE_BY_SPACE_RE.sub(' ', text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
    # -> NFD y eliminar diacríticos
    text = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", text), 0, re.I
        )

    # -> NFC
    text = normalize( 'NFC', text)
    return text


df['ejercicio'] = df['ejercicio'].apply(clean_text)

# División del dataset

X = df.ejercicio
y = df.tag
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Modelo
"""
model = Pipeline([('vect', CountVectorizer()),
                  ('tfidf', TfidfTransformer()),
                  ('clf', MultinomialNB()),
                  ])

"""

#Modelo v2
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from mlxtend.preprocessing import DenseTransformer


#Create a Gaussian Classifier
model = Pipeline([('vect', CountVectorizer()),
                  ('to_dense', DenseTransformer()),
                  ('clf', GaussianNB()),
                  ])