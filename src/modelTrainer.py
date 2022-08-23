from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
from bs4 import BeautifulSoup
import re

# Traemos los datos
df = pd.read_csv(
    'https://gist.githubusercontent.com/rgonzalezt/17ba22ffd9f7ac6c23270fd61811b8d6/raw/3ef3f58b34799fe41037923b83fc0077f320ac65/ejercicios_variados.csv')
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
    text = REPLACE_BY_SPACE_RE.sub(' ', text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
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
