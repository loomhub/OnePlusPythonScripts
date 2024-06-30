# Instructions:
# 1. Read transactionstmp from database

import pandas as pd
from dto.transaction_dto import TRANSACTIONSTMP_COLUMNS
from services.transactiontmp_filehandler import transactiontmpFileHandler
import requests

host='http://localhost:8080'    
# GET DATA FROM DATABASE
endpoint='/transactionstmp/search?period_status=open'
url=host+endpoint
output_file='DataLoads/Output/DatabaseDownloadTransactionsTmp.xlsx'

data = requests.get(url).json()
# Extract transactions from the JSON response
transactions = data.get('transactions', [])

# Create a pandas DataFrame from the transactions data
df = pd.DataFrame(transactions)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Data has been written to {output_file}")
    