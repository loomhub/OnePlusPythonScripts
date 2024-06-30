from dto.transreport_dto import TRANSREPORTS_COLUMNS
from services.transreport_filehandler import transreportFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/transreports?update=X'
url=host+endpoint
input_file='DataLoads/Prerequisite models/transreport.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'transreports'
processing_results = []

my_filehandler = transreportFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = TRANSREPORTS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    