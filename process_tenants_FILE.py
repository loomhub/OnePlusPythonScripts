from dto.tenant_dto import TENANTS_COLUMNS
from services.tenant_filehandler import tenantFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/tenants'
url=host+endpoint
input_file='DataLoads/Prerequisite models/tenants.csv'
input_folder='DataLoads/Prerequisite models/'
myObjects = 'tenants'
processing_results = []

my_filehandler = tenantFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = TENANTS_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    