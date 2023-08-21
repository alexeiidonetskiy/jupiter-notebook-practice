# main.py
from api_utils import get_cryptocurrency_data
from chart_utils import create_price_chart

def main():
    coin_id = "bitcoin"  # You can change this to any cryptocurrency's ID
    days = 7  # Number of days of data to retrieve

    timestamps, prices = get_cryptocurrency_data(coin_id, days)
    # create_price_chart(timestamps, prices, coin_id.capitalize())
    create_price_chart(timestamps, prices, coin_id.capitalize(), filename="bitcoin_price_chart", format="png")

    b'Puthon' in 'Python'
if __name__ == "__main__":
    main()
