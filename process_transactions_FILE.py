from dto.transaction_dto import TRANSACTIONS_COLUMNS
from services.transaction_filehandler import transactionFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/transactions'
url=host+endpoint
input_file='DataLoads/Transactions/transactions 2014 286.csv'
input_folder='DataLoads/Transactions/'
myObjects = 'transactions'
processing_results = []

my_filehandler = transactionFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = TRANSACTIONS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    