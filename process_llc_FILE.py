from dto.llc_dto import LLC_COLUMNS
from services.llc_filehandler import llcFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/llcs'
url=host+endpoint
input_file='DataLoads/Prerequisite models/llcs.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'llcs'
processing_results = []

my_filehandler = llcFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = LLC_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    