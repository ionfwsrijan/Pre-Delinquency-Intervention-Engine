import pandas as pd
from src.features.feature_engineering import build_features
from src.models.train_model import train_model
from src.scoring.score import score_customers

def run():
    # Placeholder data loading
    transactions = pd.read_csv("data/transactions.csv", parse_dates=["posting_date", "expected_date"])
    balances = pd.read_csv("data/balances.csv", parse_dates=["date"])
    labels = pd.read_csv("data/labels.csv")["label"]

    features = build_features(transactions, balances)
    model = train_model(features.drop(columns=["customer_id"]), labels)

    scores = score_customers(model, features.drop(columns=["customer_id"]))
    print(scores.head())

if __name__ == "__main__":
    run()