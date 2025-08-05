import json
import os

from src.external_api import convert_currency


def get_transactions_from_json(filename: str) -> list:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    try:
        with open(file_path, encoding="UTF-8") as file:
            try:
                transactions_obj = json.load(file)
            except json.JSONDecodeError:
                return []
        if type(transactions_obj) is list:
            return transactions_obj
        else:
            return []
    except FileNotFoundError:
        return []


def get_transaction_amount_rub(transaction: dict) -> float:
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
    amount = transaction.get("operationAmount", {}).get("amount", "")

    if amount == "":
        return -1
    else:
        try:
            amount_float = float(amount)
            if currency_code in ("USD", "EUR"):
                amount_rub = convert_currency(amount_float, currency_code)

                return amount_rub
            else:
                return amount_float
        except ValueError:
            return -1
