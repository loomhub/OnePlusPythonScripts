import pandas as pd
import requests

host='http://localhost:8080'

# Transreport
endpoint='/perfsummary?years=2'
#endpoint='/periodclose?update=X'
url=host+endpoint
myObjects = 'performance'
output_file='DataLoads/Output/performance_summary_report.xlsx'

data = requests.get(url).json()
df = pd.DataFrame(data)
df.to_excel(output_file, index=False)
print(f"Data has been written to {output_file}")

# Get the unique bank_account_keys
bank_account_keys = df['bank_account_key'].unique()
# Create a separate Excel file for each bank_account_key
for key in bank_account_keys:
    # Filter the DataFrame for the current bank_account_key
    df_filtered = df[df['bank_account_key'] == key]
    # Save the filtered DataFrame to an Excel file
    output_file = f"DataLoads/Output/{key}.xlsx"
    df_filtered.to_excel(output_file, index=False)
    print(f"Created {output_file}")



