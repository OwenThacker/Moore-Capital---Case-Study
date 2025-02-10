import datetime as dt
import os
import pandas as pd

# Defining the relative path dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the current script directory
csv_file = os.path.join(script_dir, "../SX7P_cleaned.csv")  # Going one level up and appending the file name

# Reading in the Data to a Pandas DataFrame
data = pd.read_csv(csv_file, index_col="Dates", parse_dates=True) 

print("CSV has successfully been read, printing data head \n")
print(data.head(5))
print(data.columns.unique()) # Used this for replacing the Quandl codes easily

# Ensure the folder exists
quandl_dir = os.path.join(script_dir, "quandl")
if not os.path.exists(quandl_dir):
    os.makedirs(quandl_dir)

# Making a loop to store data in how original Quandl data retrieval behaved
for i in range(len(data.columns)):

    ticker = data.columns[i]  # Storing the ticker name from the columns

    # Using the saved ticker variable to copy the data for that ticker
    ticker_data = data[[ticker]].copy()  
    ticker_data.columns = ['Settle']  # Renamed the column to 'Settle' to match the previous Quandl output

    # Saving the ticker data to its own CSV file within the quandl folder
    ticker_data.to_csv(
        os.path.join(quandl_dir, f"{ticker}.csv")
    )

print("Data has been successfully saved as separate CSV files.")