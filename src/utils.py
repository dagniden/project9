import json
import logging
import os

from src.external_api import get_amount_rub

current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, "..", "logs")
os.makedirs(log_dir, exist_ok=True)  # создаём папку если её нет

log_file = os.path.join(log_dir, "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_from_json(file_path: str) -> list:
    """Загружает список транзакций из JSON-файла по переданному пути файла в папке data"""
    try:
        with open(file_path, encoding="UTF-8") as file:
            try:
                transactions_obj = json.load(file)
            except json.JSONDecodeError as ex:
                logger.error(f"Error loading file: {file_path}: {ex}")
                return []
        if isinstance(transactions_obj, list):
            logger.debug("Successfully loaded transactions")
            return transactions_obj
        else:
            logger.warning("Loaded transactions is not type list")
            return []
    except FileNotFoundError as ex:
        logger.error(f"File not found: {ex}")
        return []


def get_transaction_amount_rub(transaction: dict) -> float:
    """Возвращает сумму операции в рублях, конвертируя при необходимости"""
    operation = transaction.get("operationAmount", {})
    currency_code = operation.get("currency", {}).get("code", "")
    amount = operation.get("amount", "")

    if amount == "":
        msg = "Invalid amount"
        logger.error(msg)
        raise ValueError(msg)

    try:
        amount_float = float(amount)
        if currency_code in ("USD", "EUR"):
            amount_rub = get_amount_rub(amount_float, currency_code)
            logger.debug("Successfully converted amount to rub")
            return amount_rub
        else:
            logger.debug("Successfully returned amount rub without conversion")
            return amount_float
    except ValueError as ex:
        logger.error(f"Invalid amount: {ex}")
        raise ValueError("Invalid amount")
