import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from mlxtend.preprocessing import DenseTransformer
nltk.download('stopwords')
import re
from unicodedata import normalize

# Traemos los datos
df = pd.read_csv('https://gist.githubusercontent.com/rgonzalezt/5441c29e680d92b6f717aead7cc25b73/raw/83afafe5ece6cce14f5595b81eb05960075faac3/ejercicios_modelo_24_11.csv')

df = df[pd.notnull(df['tag'])]

# Limpieza de datos
STOPWORDS = set(stopwords.words('spanish'))


def clean_text(text):
    """
        text: a string

        return: modified initial string
    """
    text = text.lower()  # lowercase text
    #text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
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

model = Pipeline([('vect', CountVectorizer()),
                  ('to_dense', DenseTransformer()),
                  ('clf', GaussianNB()),
                  ])