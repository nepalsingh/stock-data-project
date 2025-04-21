import pandas as pd
import random
from datetime import datetime, timedelta


def generate_stock_data(start_date, end_date, stock_name, output_file):
    """
    Generate sample daily stock data and save it to a CSV file.

    :param start_date: Start date for the data (YYYY-MM-DD)
    :param end_date: End date for the data (YYYY-MM-DD)
    :param stock_name: Name of the stock
    :param output_file: Path to the output CSV file
    """
    # Generate a list of dates between start_date and end_date
    date_range = pd.date_range(start=start_date, end=end_date)

    # Generate random stock data
    data = []
    for date in date_range:
        low_price = round(random.uniform(100, 120), 2)
        high_price = round(random.uniform(low_price, low_price + 20), 2)
        close_price = round(random.uniform(low_price, high_price), 2)
        volume = random.randint(10000000, 20000000)
        data.append([date.strftime('%Y-%m-%d'),  close_price, volume])

    # Create a DataFrame
    df = pd.DataFrame(
        data, columns=['Date', 'Close',  'Volume'])

    # Add a stock name column
    df['Stock'] = stock_name

    # Save to CSV
    df.to_csv(output_file, index=False, header=True)
    print(f"Stock data for {stock_name} saved to {output_file}")


# Example usage
if __name__ == "__main__":

    # add command line arguments to the script
    import argparse
    parser = argparse.ArgumentParser(description='Generate stock data.')

    parser.add_argument('--stock_name', type=str, required=True,
                        help='Name of the stock')
    stock_name = parser.parse_args().stock_name

    generate_stock_data(
        start_date="2020-01-01",
        end_date="2023-12-31",
        stock_name=stock_name,
        output_file=f"/Users/nepalsingh/Desktop/warea/project/taapeylabs/stockprice_homeproject/stocks-{stock_name.lower()}.csv"
    )


# python create-data.py --stock_name NVDA
# python create-data.py --stock_name GOOG
# python create-data.py --stock_name APPL
# python create-data.py --stock_name MSFT
# python create-data.py --stock_name AMZN
