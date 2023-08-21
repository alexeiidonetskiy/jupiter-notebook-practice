# api_utils.py
import requests

def get_cryptocurrency_data(coin_id, days):
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = f"/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()

    timestamps = [entry[0] for entry in data["prices"]]
    prices = [entry[1] for entry in data["prices"]]

    return timestamps, prices
