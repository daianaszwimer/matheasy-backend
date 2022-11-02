import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nltk.download('stopwords')
from bs4 import BeautifulSoup
import re
from unicodedata import normalize

# Traemos los datos
df = pd.read_csv('https://gist.githubusercontent.com/rgonzalezt/525494fb91010b362eceaa1d0c9368eb/raw/5d00c08c53a7e2a46c250e1b7bb27e29f9bd5c8a/ejercicios_modelo_1_11.csv')

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo

model = Pipeline([('vect', CountVectorizer()),
                  ('tfidf', TfidfTransformer()),
                  ('clf', MultinomialNB()),
                  ])
