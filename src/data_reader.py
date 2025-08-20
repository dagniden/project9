import pandas as pd
import os


def get_transactions_csv(filename: str) -> list:
    df = pd.read_csv(filename)
    return df.to_dict(orient='records')


def get_transactions_xls(filename: str) -> list:
    df = pd.read_excel(filename)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    csv_file = os.path.join(data_dir, "transactions.csv")
    xls_file = os.path.join(data_dir, "transactions_excel.xlsx")

    csv_dict = get_transactions_csv(csv_file)
    print(csv_dict)

    # xls_dict = get_transactions_xls(xls_file)
    # print(xls_dict)
