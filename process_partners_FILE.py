from dto.partner_dto import PARTNERS_COLUMNS
from services.partner_filehandler import partnerFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/partners'
url=host+endpoint
input_file='DataLoads/Prerequisite models/partners.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'partners'
processing_results = []

my_filehandler = partnerFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = PARTNERS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    