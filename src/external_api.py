import os

import requests
from dotenv import load_dotenv


def convert_currency(amount: float, currency_from: str, currency_to: str = "RUB"):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    print("API KEY:", api_key)

    if not api_key:
        raise ValueError("API key not found in environment variables.")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    headers = {"apikey": api_key}
    print("URL:", url)
    print("Headers:", headers)

    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code != 200:
        raise ValueError("Failed to get conversion from external API")

    result_amount = response.json().get("result")
    if not result_amount:
        raise ValueError("No data from conversion with external API")

    return result_amount


if __name__ == "__main__":
    print(convert_currency(amount=8463.45, currency_from="USD"))
