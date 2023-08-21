# chart_utils.py
import matplotlib.pyplot as plt

def create_price_chart(timestamps, prices, coin_name, filename=None, format='png'):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker='o')
    plt.title(f"{coin_name} Price Chart")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    

    if filename:
        full_filename = f"{filename}.{format}"
        plt.savefig(full_filename, format=format)
        print(f"Chart saved as {full_filename}")
    else:
        plt.show()
