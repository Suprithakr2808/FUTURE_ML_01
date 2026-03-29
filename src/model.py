import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.preprocess import clean_text

def train_model():
    df = pd.read_csv("data/tickets.csv")

    df['cleaned'] = df['ticket'].apply(clean_text)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['cleaned'])
    y = df['category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, vectorizer