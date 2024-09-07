# Test http://0.0.0.0:8080/docs to confirm the server is running
# If not, open folder fastapi-oneplus and run main.py

# Instructions:
# 1. If transactionstmp table is empty:
#  1a. Copy "Transactions/transactionstmp_template.csv" to "Transactions/transactionstmp.csv"
#  1b. Run the script. You may see Error: Input records don't match output records. This is normal.
#  1c. Save xls file as csv from "/Output/DatabaseDownloadTransactionstmp.xls" to "Transactions/transactionstmp.csv"

# 2. If transactionstmp table is not empty:
#  2a. Review "Transactions/transactionstmp.csv" file and update classification = 'clean' for records that are clean
#  2b. If necessary, run update_rules_FILE.py to update rules
#  2c. Run the script
#  2d. Save xls file as csv from "/Output/DatabaseDownloadTransactionstmp.xls" to "Transactions/transactionstmp.csv"

# Logic
# 1. Read transactionstmp, transactions, bankDownloads, recordsDF (user updates on load file)
# 2. Drop records from recordsDF, bankDownloads, transactionstmp 
#    where tdate < max tdate for each bank_account_key in transactions table
# 3. Initialize newDF from bankdownloads data
        # columns_to_initialize = ['vendor_no_w9', 'customer_no_w9','comments']
        # df.loc[:, columns_to_initialize] = 'Initial'
        # df.loc[:, 'transaction_group'] = 'X-Review'
        # df.loc[:, 'transaction_type'] = 'Review'
        # df.loc[:, 'vendor'] = 'GeneralVendor'
        # df.loc[:, 'customer'] = 'GeneralCustomer'
        # df.loc[:, 'classification'] = 'review'
        # df.loc[:, 'period_status'] = 'open'
# 4. Merge newDF with information from recordsDF and transtmpDF
# 5. loop at newDF. 
#      if transtmpDF.classification = 'clean', overwrite newDF from transtmp
#      elif recordtmpDF.classification exists, overwrite newDF from recordDF
#    drop merged_columns from newDF
# 6. Apply business rules to newDF records where classification != 'clean'
# 7. Post newDF to transactionstmp table
import pandas as pd
from dto.transaction_dto import TRANSACTIONSTMP_COLUMNS, transactionDTO
from services.transactiontmp_filehandler import transactiontmpFileHandler
import requests

host='http://localhost:8080'

# APPLY RULES
endpoint='/applyrules?update=X'
url=host+endpoint
input_file='DataLoads/Transactions/transactionstmp.csv'
input_folder='DataLoads/Transactions/'
myObjects = 'transactions'
processing_results = []


my_filehandler = transactiontmpFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = TRANSACTIONSTMP_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
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
    