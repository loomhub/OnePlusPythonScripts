import pandas as pd
import requests
host='http://localhost:8080'
#{{hostName}}/transactions/search?start_date=1990-12-31&end_date=2013-12-31
# Bank Downloads
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