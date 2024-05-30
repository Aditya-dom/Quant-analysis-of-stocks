## Instructions:

This test is designed to evaluate your proficiency in using Pandas for data manipulation tasks.
You are required to write Python code using Pandas to solve each task.
Make sure your code is efficient, well-structured, and handles exceptions appropriately.
Provide comments where necessary to explain your thought process.
Submit your solutions as a single Python file and output files.

### Task 1: Data Exploration and Manipulation

Given a CSV file stocks.csv containing daily stock price data with columns date, open, high, low, close, volume, Name perform the following tasks:

a) Read the data into a Pandas DataFrame.
b) Calculate the average closing price (close) for each unique ticker and save the data in stock_data.csv with name, avgPrice as columns.
c) Calculate the daily percentage change in the closing price (close) for each ticker and save seperate csv in data/{Name}.csv

### Task 2: Time Series Analysis

Given the same stocks.csv dataset, perform the following tasks:

a) Resample the data to a monthly frequency, taking the average of Open, High, Low, Close, and summing Volume and save seperate csv in monthData/{Name}.csv.
b) Calculate the rolling 30-day average of the closing price (Close) for each ticker and a column in data/{Name}.csv.

### Task 3: Data Merging and Joining

Given two CSV files: fundamentals.csv containing fundamental data like Ticker, MarketCap, and Sector, and prices.csv containing price data like Ticker and Price, perform the following tasks:

a) Read both files into separate Pandas DataFrames.
b) Merge the two DataFrames on the Ticker column.
c) Calculate the market capitalization (MarketCap) to price ratio for each ticker and save the csv as stockInfo.csv

### Task 4: Performance Analysis

a) Read the data of each ticker (stocks.csv) into a Pandas DataFrame.
b) Calculate daily profit/loss on each ticker assuming stock has been bought with 1 quantity on the first day and add a column 'pnl'
c) Calculate and add cumulative profit/loss column
d) Calculate and add the drawdown column
e) Added column must reflect on data/{Name}.csv


Submission:

Submit your solution as a Python file and output files along with a README file explaining any assumptions made, how to run the code, and any additional comments you'd like to add about your implementation choices.

#


