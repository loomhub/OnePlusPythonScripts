from dto.bank_download_dto import WELLSFARGO_COLUMNS, WELLSFARGO_FILEHEADERS
from services.bank_download_filehandler import bankdownloadFileHandler

host='http://localhost:8080'

# Bank Downloads
endpoint='/bankdownloads'
url=host+endpoint
input_file='DataLoads/BankDownloads/wellsfargo/104Meadow.csv'
input_folder='DataLoads/BankDownloads/wellsfargo/'
myObjects = 'bankdownloads'
processing_results = []

my_filehandler = bankdownloadFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = WELLSFARGO_COLUMNS,
        rename_columns = None,
        fileheaders = WELLSFARGO_FILEHEADERS)

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    