from dto.bankaccount_dto import BANK_ACCOUNTS_COLUMNS
from services.bankaccount_filehandler import bankaccountFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/bankaccounts'
url=host+endpoint
input_file='DataLoads/Prerequisite models/bankaccounts.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'bankaccounts'
processing_results = []

my_filehandler = bankaccountFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = BANK_ACCOUNTS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    