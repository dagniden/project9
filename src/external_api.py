import os

import requests
from dotenv import load_dotenv


def convert_currency(amount: float, currency_from: str, currency_to: str = "RUB"):
    load_dotenv()

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=&from={currency_from}&amount={amount}"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError("Failed to get conversion from external api")

    result_amount = response.json().get("result")
    if not result_amount:
        raise ValueError("No data from conversion with external api")

    return result_amount
