import pandas as pd


def get_transactions_csv(filename: str) -> list:
    """Функция для считывания финансовых операций из CSV"""
    df = pd.read_csv(filename, encoding="utf-8", sep=";")
    return df.to_dict(orient="records")


def get_transactions_xls(filename: str) -> list:
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel(filename)
    return df.to_dict(orient="records")
