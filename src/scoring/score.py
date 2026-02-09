import pandas as pd

def score_customers(model, features: pd.DataFrame) -> pd.DataFrame:
    """
    Return risk scores for each customer.
    """
    risk_score = model.predict_proba(features)[:, 1]
    results = features.copy()
    results["risk_score"] = risk_score
    return results
