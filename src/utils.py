import os
import json
import requests


def get_transactions_from_json(filename: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    try:
        with open(file_path, encoding="UTF-8") as file:
            try:
                transactions_obj = json.load(file)
            except json.JSONDecodeError:
                return []
        if type(transactions_obj) == list:
            return transactions_obj
        else:
            return []
    except FileNotFoundError:
        return []


