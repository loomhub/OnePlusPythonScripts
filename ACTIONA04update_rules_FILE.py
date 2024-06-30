# Instructions:
# 1. Make changes to BusinessRules.csv file to update rules.
# 2. Run the script

import requests
from dto.rule_dto import RULES_COLUMNS
from services.rule_filehandler import ruleFileHandler

host='http://localhost:8080'

endpoint = '/rulestruncate'
url=host+endpoint
response = requests.delete(url)
output_data = response.json()  # Convert the response to JSON format

# Rules load
endpoint='/rules?update=X'
url=host+endpoint
input_file='DataLoads/Transactions/BusinessRules.csv'
input_folder='DataLoads/Transactions/'
myObjects = 'rules'
processing_results = []

my_filehandler = ruleFileHandler(file=input_file)

processing_results = my_filehandler.process_files(url, myObjects,
        column_names = RULES_COLUMNS,
        rename_columns = 'X')

for dct in processing_results:
    formatted_string = ' '.join(f"{key}: {value}" for key, value in dct.items())
    print(formatted_string)
    
    