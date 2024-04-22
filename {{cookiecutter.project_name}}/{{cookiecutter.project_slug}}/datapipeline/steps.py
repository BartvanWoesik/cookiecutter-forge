import pandas as pd

def multiply(df: pd.DataFrame, column: str):
    df["multiply"] = df[[column]] * 2
    return df