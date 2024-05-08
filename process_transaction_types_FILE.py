from dto.transaction_type_dto import TRANSACTION_TYPES_COLUMNS
from services.transaction_type_filehandler import transactionTypeFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/transactionTypes'
url=host+endpoint
input_file='DataLoads/Prerequisite models/TransactionTypes.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'transactionTypes'
processing_results = []

my_filehandler = transactionTypeFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = TRANSACTION_TYPES_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    