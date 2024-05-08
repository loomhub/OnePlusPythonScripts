from dto.bank_download_dto import CHASE_COLUMNS, CHASE_FILEHEADERS
from services.bank_download_filehandler import bankdownloadFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/bankdownloads'
url=host+endpoint
input_file='DataLoads/BankDownloads/chase/Common.CSV'
input_folder='DataLoads/BankDownloads/chase/'
myObjects = 'bankdownloads'
processing_results = []

my_filehandler = bankdownloadFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = CHASE_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    