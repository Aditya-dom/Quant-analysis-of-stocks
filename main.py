import os
import logging
from data_processing import (
    read_data, calculate_avg_close_price, calculate_daily_percentage_change, resample_data,
    calculate_rolling_average, merge_data, calculate_market_capitalization, calculate_profit_loss,
    calculate_cumulative_profit_loss, calculate_drawdown, save_data, plot_data
)

def main():
    try:
        # Task 1: Data Exploration and Manipulation
        stocks_file_path = 'stocks.csv'
        if not os.path.exists(stocks_file_path):
            logging.error(f"File not found: {stocks_file_path}")
            return

        data = read_data(stocks_file_path)

        # Part (b): Calculate the average closing price for each unique ticker and save the data
        avg_close_price = calculate_avg_close_price(data)
        save_data(avg_close_price, 'stock_data.csv')

        # Part (c): Calculate the daily percentage change in the closing price for each ticker and save separately
        data = calculate_daily_percentage_change(data)
        for name, group in data.groupby('Name'):
            save_data(group, f'data/{name}.csv')

        # Task 2: Time Series Analysis
        resampled_data = resample_data(data)
        for name, group in resampled_data.groupby('Name'):
            save_data(group, f'monthData/{name}.csv')

        # Calculate the rolling 30-day average of the closing price for each ticker
        data = calculate_rolling_average(data)
        for name, group in data.groupby('Name'):
            save_data(group, f'data/{name}.csv')

        # Task 3: Data Merging and Joining
        fundamentals_file_path = 'fundamentals.csv'
        prices_file_path = 'prices.csv'

        if not os.path.exists(fundamentals_file_path) or not os.path.exists(prices_file_path):
            logging.error("One or both of the required files for Task 3 are missing.")
            return

        fundamentals = read_data(fundamentals_file_path)
        prices = read_data(prices_file_path)

        merged_data = merge_data(fundamentals, prices)
        stock_info = calculate_market_capitalization(merged_data)
        save_data(stock_info, 'stockInfo.csv')

        # Task 4: Performance Analysis
        data = calculate_profit_loss(data)
        data = calculate_cumulative_profit_loss(data)
        data = calculate_drawdown(data)
        for name, group in data.groupby('Name'):
            save_data(group, f'data/{name}.csv')

        # Plotting data for visualization
        plot_data(data, 'cumulative_pnl', 'Cumulative Profit and Loss', 'plots/cumulative_pnl.png')
        plot_data(data, 'drawdown', 'Drawdown', 'plots/drawdown.png')

    except Exception as e:
        logging.error(f"An error occurred in the script: {e}")

if __name__ == '__main__':
    main()
