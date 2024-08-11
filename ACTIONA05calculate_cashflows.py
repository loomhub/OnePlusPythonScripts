# Test http://0.0.0.0:8080/docs to confirm the server is running
# If not, open folder fastapi-oneplus and run main.py

# Instructions:
# 1. Run the script
# 2. File 'DataLoads/Output/cashflows.xlsx' will now contain the calculated balances for review

# Logic
#1. Load cashflowsDF and transactionstmpDF
#2. Clean data in cashflowsDF and transactionstmpDF
#3. cashflowsDataDF = cashflowsDataDF[cashflowsDataDF['period_status'] == 'closed']
#4. lastrowsDF = records from cashflowDF with max(start_date)
#5. Build newcashflowsDF = rows from transactionstmpDF where tdate > lastrowsDF['start_date'] for each bank_account_balance
#6. Add start_date and end_date to newcashflowsDF
#7. Pivot records from transactionstmp to calculate cash_change for each month, starting balance and ending balance
# 8. Update cashflows datable    


import pandas as pd
import requests
host='http://localhost:8080'
#{{hostName}}/transactions/search?start_date=1990-12-31&end_date=2013-12-31
# Bank Downloads
endpoint='/cashflows/calculate?update=X'
url=host+endpoint
data = requests.post(url).json()


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