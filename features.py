from db import load_data

def get_features():
    df = load_data()

    df["utilization_ratio"] = df["current_balance"] / df["credit_limit"]

    df["spending_to_income_ratio"] = (
        df["current_balance"] / df["annual_income"]
    )

    df["income_to_credit"] = df["annual_income"] / df["credit_limit"]

    df["risk_score"] = (
        df["utilization_ratio"] * 0.5
        + (1 / (df["income_to_credit"] + 1e-6)) * 0.3
        + (1 / (df["num_products"] + 1)) * 0.2
    )

    return df