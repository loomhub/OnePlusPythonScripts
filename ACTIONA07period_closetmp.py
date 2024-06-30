# Instructions
# 1. Run the script to set period_status = 'closed' for all rows in transactionstmp where cashflow table has closed period

import pandas as pd
import requests
from dto.cashflow_dto import CASHFLOWS_COLUMNS
from services.cashflow_filehandler import cashflowFileHandler

host='http://localhost:8080'

# Bank Downloads
#endpoint='/periodclose'
endpoint='/periodclosetmp?update=X'
url=host+endpoint
myObjects = 'transactions'
output_file='DataLoads/Output/closedtransactionstmp.xlsx'

data = requests.post(url).json()
# Extract the 'transactions' values
transactions_data = [item['transactions'] for item in data]
df = pd.DataFrame(transactions_data)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)
print(f"Data has been written to {output_file}")

