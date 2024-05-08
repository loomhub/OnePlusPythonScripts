from dto.balance_dto import BALANCES_COLUMNS
from services.balance_filehandler import balanceFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/balances'
url=host+endpoint
input_file='DataLoads/Prerequisite models/balances.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'balances'
processing_results = []

my_filehandler = balanceFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = BALANCES_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    