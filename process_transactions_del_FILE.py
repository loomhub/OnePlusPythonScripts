from dto.transaction_dto import TRANSACTIONS_DEL_COLUMNS
from services.transaction_filehandler import transactionFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/transactionsdel'
url=host+endpoint
input_file='DataLoads/Transactions/transactionsDelete.csv'
input_folder='DataLoads/Transactions/'
myObjects = 'transactionsDel'
processing_results = []

my_filehandler = transactionFileHandler(file=input_file)

processing_results = my_filehandler.delete_using_filedata(url, myObjects,
        column_names = TRANSACTIONS_DEL_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
