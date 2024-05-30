import pandas as pd
import os
import logging
import matplotlib.pyplot as plt
from typing import List
from pandas.core.frame import DataFrame
from numba import njit
import numpy as np

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create necessary directories if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('monthData', exist_ok=True)
os.makedirs('plots', exist_ok=True)

def read_data(file_path: str, parse_dates: bool = False) -> DataFrame:
    """
    Read the data from the given file path
    :param file_path: str: Path of the file
    :param parse_dates: bool: Whether to parse 'date' column
    :return: DataFrame: Data read from the file
    """
    try:
        data = pd.read_csv(file_path)
        if parse_dates:
            if 'date' not in data.columns:
                logging.error(f"Missing 'date' column in file: {file_path}")
                raise KeyError("Missing 'date' column")
            data['date'] = pd.to_datetime(data['date'])
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logging.error(f"File is empty: {file_path}")
        raise
    except KeyError as e:
        logging.error(f"Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        raise

def calculate_avg_close_price(data: DataFrame) -> DataFrame:
    """
    Calculate the average closing price for each unique ticker
    :param data: DataFrame: Data to calculate the average closing price
    :return: DataFrame: Data with average closing price
    """
    return data.groupby('Name')['close'].mean().reset_index()

@njit
def pct_change(close):
    pct_changes = np.empty(close.shape[0] - 1)
    for i in range(close.shape[0] - 1):
        pct_changes[i] = (close[i + 1] - close[i]) / close[i]
    return pct_changes

def calculate_daily_percentage_change(data: DataFrame) -> DataFrame:
    """
    Calculate the daily percentage change in the closing price for each ticker
    :param data: DataFrame: Data to calculate the daily percentage change
    :return: DataFrame: Data with daily percentage change
    """
    data['daily_percentage_change'] = np.nan
    for name, group in data.groupby('Name'):
        pct_changes = pct_change(group['close'].values)
        data.loc[group.index[1:], 'daily_percentage_change'] = pct_changes
    return data

def resample_data(data: DataFrame) -> DataFrame:
    """
    Resample the data to a monthly frequency
    :param data: DataFrame: Data to resample
    :return: DataFrame: Data with resampled data
    """
    data['date'] = pd.to_datetime(data['date'])
    resampled = data.set_index('date').groupby('Name').resample('M').agg({
        'open': 'mean',
        'high': 'mean',
        'low': 'mean',
        'close': 'mean',
        'volume': 'sum'
    }).reset_index()
    return resampled

def calculate_rolling_average(data: DataFrame) -> DataFrame:
    """
    Calculate the rolling 30-day average of the closing price for each ticker
    :param data: DataFrame: Data to calculate the rolling 30-day average
    :return: DataFrame: Data with rolling 30-day average
    """
    data['rolling_30_day_avg'] = data.groupby('Name')['close'].transform(lambda x: x.rolling(window=30).mean())
    return data

def merge_data(data1: DataFrame, data2: DataFrame) -> DataFrame:
    """
    Merge the two DataFrames on the Ticker column
    :param data1: DataFrame: First DataFrame
    :param data2: DataFrame: Second DataFrame
    :return: DataFrame: Merged DataFrame
    """
    return pd.merge(data1, data2, on='Ticker')

def calculate_market_capitalization(data: DataFrame) -> DataFrame:
    """
    Calculate the market capitalization to price ratio for each ticker
    :param data: DataFrame: Data to calculate the market capitalization to price ratio
    :return: DataFrame: Data with market capitalization to price ratio
    """
    data['market_capitalization_to_price_ratio'] = data['MarketCap'] / data['Price']
    return data

def calculate_profit_loss(data: DataFrame) -> DataFrame:
    """
    Calculate daily profit/loss on each ticker assuming stock has been bought with 1 quantity on the first day
    :param data: DataFrame: Data to calculate the profit/loss
    :return: DataFrame: Data with profit/loss
    """
    data['pnl'] = data.groupby('Name')['close'].diff().fillna(0)
    return data

def calculate_cumulative_profit_loss(data: DataFrame) -> DataFrame:
    """
    Calculate cumulative profit/loss
    :param data: DataFrame: Data to calculate the cumulative profit/loss
    :return: DataFrame: Data with cumulative profit/loss
    """
    data['cumulative_pnl'] = data.groupby('Name')['pnl'].cumsum()
    return data

def calculate_drawdown(data: DataFrame) -> DataFrame:
    """
    Calculate the drawdown
    :param data: DataFrame: Data to calculate the drawdown
    :return: DataFrame: Data with drawdown
    """
    data['peak'] = data.groupby('Name')['cumulative_pnl'].cummax()
    data['drawdown'] = (data['cumulative_pnl'] - data['peak']) / data['peak']
    return data

def save_data(data: DataFrame, file_path: str):
    """
    Save the data to the given file path
    :param data: DataFrame: Data to save
    :param file_path: str: Path to save the data
    """
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        logging.error(f"Error saving file {file_path}: {e}")
        raise


def plot_data(data: DataFrame, column: str, title: str, output_path: str):
    """
    Plot the data for a specific column
    :param data: DataFrame: Data to plot
    :param column: str: Column to plot
    :param title: str: Title of the plot
    :param output_path: str: Path to save the plot
    """
    try:
        plt.figure(figsize=(10, 6))
        for name, group in data.groupby('Name'):
            plt.plot(group['date'], group[column], label=name)
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        logging.error(f"Error plotting data: {e}")
        raise
