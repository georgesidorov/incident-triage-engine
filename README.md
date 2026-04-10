# Incident Triage Engine

A machine‑learning tool that classifies IT incidents and assigns a priority score. Users can train their own model using the included dataset or run predictions using the provided scripts.

## Technical Overview

The engine combines classical machine‑learning with lightweight rule‑based logic to classify incident descriptions and assign priority levels. It is designed to be fast, interpretable, and easy to retrain.

### Machine Learning Components
- Text vectorisation using a bag‑of‑words model.
- N‑gram features (unigrams and bigrams) to capture meaningful word patterns.
- Train/test split for evaluating model performance.
- Logistic Regression for multi‑class text classification.
- Model persistence using joblib (model.pkl, vectorizer.pkl).

### Prediction Pipeline
- Text preprocessing and vectorisation.
- Category prediction using the trained classifier.
- Confidence scoring via class probability outputs.

### Priority Logic
- Rule‑based scoring using keywords and severity indicators.
- Fallback logic to ensure safe, meaningful output when confidence is low.

### Engineering Features
- Logging of predictions, errors, and training events (logs/ directory, ignored by Git).
- Fully reproducible training using the included dataset and train.py.

## Documentation

For a detailed explanation of the techniques used (TF‑IDF, n‑grams, Logistic Regression, priority logic, fallback behaviour), see:

**/why-these-methods.md**

## Features
- Train a text classification model using `train.py`
- Predict incident categories and priority using `predict.py`
- Includes dataset for reproducible training
- Clean project structure with logs ignored via `.gitignore`

## Installation
Create a virtual environment and install dependencies:
> pip install -r requirements.txt

## Training the Model
Generate `model.pkl` and `vectorizer.pkl`:
> python src/train.py

The trained model will be saved in the `models/` directory.

## Running Predictions
Classify an incident description:
> python src/predict.py "The server is down and users cannot log in"

## Project Structure
1. incident-triage/src/train.py
2. incident-triage/src/predict.py
3. incident-triage/data/dataset.csv
4. incident-triage/models/model.pkl
5. incident-triage/models/vectorizer.pkl
6. incident-triage/logs/triage.log        (ignored by .gitignore)
7. incident-triage/why-these-methods.md
8. incident-triage/requirements.txt
9. incident-triage/.gitignore
10. incident-triage/README.md

## Future Improvements
- Expand dataset with more incident types
- Add web UI for interactive triage
