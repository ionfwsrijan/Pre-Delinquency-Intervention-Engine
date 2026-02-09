from dataclasses import dataclass
import pandas as pd

@dataclass
class FeatureConfig:
    """Configuration for feature engineering thresholds (future use)."""
    salary_delay_threshold_days: int = 3
    savings_drop_pct_threshold: float = 0.2

def build_features(transactions: pd.DataFrame, balances: pd.DataFrame) -> pd.DataFrame:
    """
    Build behavioral features used for early-risk prediction.
    """
    # Example: salary delay feature
    salary_txn = transactions[transactions["category"] == "salary"]
    salary_txn["salary_delay_days"] = (
        salary_txn["posting_date"] - salary_txn["expected_date"]
    ).dt.days

    # Example: savings drop feature
    balances["savings_drop_pct"] = balances.groupby("customer_id")["balance"].pct_change()

    features = pd.merge(
        salary_txn[["customer_id", "salary_delay_days"]],
        balances[["customer_id", "savings_drop_pct"]],
        on="customer_id",
        how="inner",
    )

    return features
