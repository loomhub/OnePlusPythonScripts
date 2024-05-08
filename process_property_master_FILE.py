from dto.property_master_dto import PROPERTY_MASTER_COLUMNS
from services.property_master_filehandler import propertyMasterFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/propertyMasters'
url=host+endpoint
input_file='DataLoads/Prerequisite models/property_master.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'propertyMasters'
processing_results = []

my_filehandler = propertyMasterFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = PROPERTY_MASTER_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    