# Test http://0.0.0.0:8080/docs to confirm the server is running
# If not, open folder fastapi-oneplus and run main.py

# Instructions
# 1. Check the bank statements. Populate ending_balances. Period_status = 'closed' if ending_balance = calc_balance
# 2. Prepare a load file "DataLoads/Prerequisite models/cashflowsAug022024.csv"
# 3. Run the script

# Logic
#1. The code fills in gap months with cash_change = 0 and ending_balance = prev_balance

import pandas as pd
import requests
from dto.cashflow_dto import CASHFLOWS_COLUMNS
from services.cashflow_filehandler import cashflowFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/cashflows?update=X'
url=host+endpoint
input_file='DataLoads/Prerequisite models/cashflowsAug022024.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'cashflows'
processing_results = []

my_filehandler = cashflowFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = CASHFLOWS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)

# GET DATA FROM DATABASE
endpoint='/cashflows'
url=host+endpoint
output_file='DataLoads/Output/cashflows.xlsx'

data = requests.get(url).json()
# Extract transactions from the JSON response
transactions = data.get('cashflows', [])

# Create a pandas DataFrame from the transactions data
df = pd.DataFrame(transactions)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Data has been written to {output_file}")
    
    