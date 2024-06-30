# Instructions:
# 1. Download Chase bankdata to Chase folder. 
# 2. Make sure to name the files after property names. This is how the program knows which property the bankdata belongs to.
# 3. Run this script.
from dto.bank_download_dto import CHASE_COLUMNS
from services.bank_download_filehandler import bankdownloadFileHandler


host='http://localhost:8080'

# Bank Downloads
endpoint='/bankdownloads'
url=host+endpoint
#input_file='DataLoads/BankDownloads/chase/114Sidney.CSV'
input_folder='DataLoads/BankDownloads/chase/'
myObjects = 'bankdownloads'
processing_results = []

my_filehandler = bankdownloadFileHandler(folder=input_folder)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = CHASE_COLUMNS,
        rename_columns = 'X',
        fileheaders = None)

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    

    