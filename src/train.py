import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def main():
    # Load dataset
    data = pd.read_csv("data/incidents.csv")

    # Split into features and labels
    X = data["description"]
    y = data["category"]

    # Convert text to TF-IDF vectors
    # Model becomes sufficiently confident after dataset expansion + n‑grams
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.9
    )
    X_vectors = vectorizer.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_vectors, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    
    joblib.dump(model, "models/model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")

if __name__ == "__main__":
    main()
