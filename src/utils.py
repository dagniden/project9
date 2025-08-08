import json

from src.external_api import get_amount_rub


def get_transactions_from_json(file_path: str) -> list:
    """Загружает список транзакций из JSON-файла по переданному пути файла в папке data"""
    try:
        with open(file_path, encoding="UTF-8") as file:
            try:
                transactions_obj = json.load(file)
            except json.JSONDecodeError:
                return []
        if isinstance(transactions_obj, list):
            return transactions_obj
        else:
            return []
    except FileNotFoundError:
        return []


def get_transaction_amount_rub(transaction: dict) -> float:
    operation = transaction.get("operationAmount", {})
    currency_code = operation.get("currency", {}).get("code", "")
    amount = operation.get("amount", "")

    if amount == "":
        raise ValueError("Invalid amount")

    try:
        amount_float = float(amount)
        if currency_code in ("USD", "EUR"):
            return get_amount_rub(amount_float, currency_code)
        else:
            return amount_float
    except ValueError:
        raise ValueError("Invalid amount")
