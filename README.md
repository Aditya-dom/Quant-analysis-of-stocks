# Stock Data Analysis
This project is designed for quantitative analysis of stock data, covering various aspects from data manipulation to performance analysis. Below are instructions on how to run the code, assumptions made during development, and additional notes on implementation choices.

## Project Structure
``` 
Quant-analysis-of-stocks/
├── main.py
├── data_processing.py
├── data/
└── monthData/

Add datasets in csv format which provided.
```

## How to Run the Code
Environment Setup:

Ensure Python 3.x is installed on your machine.
Install required packages by running `pip install -r requirements.txt` in your terminal.
Input Data:

Place your data files ('stocks.csv', 'fundamentals.csv', 'prices.csv') in the root directory of the project.
Execution:

Open a terminal or command prompt.
Navigate to the project directory.
Run the command: `python main.py`
Output:

Results will be saved in the following directories:
stock_data.csv: Average closing prices for each ticker.
data/{name}.csv: Daily percentage changes for each ticker.
monthData/{name}.csv: Resampled monthly data for each ticker.
stockInfo.csv: Calculated market capitalization data.
data/{name}.csv: Performance metrics (profit/loss, cumulative P/L, drawdowns) for each ticker.
Plots:
plots/cumulative_pnl.png: Cumulative Profit and Loss visualization.
plots/drawdown.png: Drawdown visualization.
Assumptions Made
Data Consistency: It is assumed that input data files ('stocks.csv', 'fundamentals.csv', 'prices.csv') are correctly formatted with necessary columns ('Ticker', 'Date', 'Close', 'Shares Outstanding', 'Price').

Date Parsing: Dates in the input data are assumed to be in a format compatible with Pandas datetime parsing.

## Additional Notes
Error Handling: The code includes robust error handling to manage scenarios like missing files, missing columns, and data processing errors. Errors are logged with details to aid in debugging.

Performance: Utilization of Pandas for data manipulation ensures efficient handling of large datasets. NumPy and Numba are used for optimized numerical computations where applicable.

Extendability: The project can be extended by adding new functions in data_processing.py for additional analyses or modifying existing functions to accommodate different data structures or computations.



## Summary of Implementation
This project focuses on quantitative analysis of stock data, including data exploration, manipulation, time series analysis, data merging, and performance analysis. The main tasks covered are:

### Data Exploration and Manipulation:

Reading stock data from 'stocks.csv'.
Calculating average closing prices and daily percentage changes for each ticker.
Resampling data to monthly frequency and calculating rolling averages.
Data Merging and Joining:

Merging fundamental data from 'fundamentals.csv' and price data from 'prices.csv' based on a common identifier ('Ticker').
Calculating market capitalization based on 'Shares Outstanding' and 'Price'.
Performance Analysis:

Calculating profit/loss, cumulative profit/loss, and drawdowns for each ticker.
Saving individual ticker data and plotting cumulative profit/loss and drawdowns.
Key Components and Functions
Data Processing (data_processing.py):

Includes functions for reading data, calculating averages, percentage changes, resampling, merging, market capitalization, profit/loss, cumulative profit/loss, drawdowns, saving data, and plotting.
Main Script (main.py):

Executes the workflow by sequentially calling functions defined in data_processing.py.
Handles file existence checks and error logging.
Assumptions Made
Data Consistency: It is assumed that input data ('stocks.csv', 'fundamentals.csv', 'prices.csv') are structured with expected columns ('Ticker', 'Date', 'Close', 'Shares Outstanding', 'Price') and that they are consistent in format and structure.

Performance Considerations: Utilizing Pandas for data manipulation ensures efficient handling of large datasets, while NumPy and Numba optimize specific computations for performance where applicable.

Extendability: The code can be extended by adding more functions in data_processing.py for additional analyses or by modifying existing functions to accommodate different data formats or calculations.

#
