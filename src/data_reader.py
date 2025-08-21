import pandas as pd


def get_transactions_csv(filename: str) -> list:
    df = pd.read_csv(filename)
    return df.to_dict(orient="records")


def get_transactions_xls(filename: str) -> list:

    df = pd.read_excel(filename)
    return df.to_dict(orient="records")
