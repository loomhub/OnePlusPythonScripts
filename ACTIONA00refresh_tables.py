# Instructions:
# 1. Run the script to truncate transactiontmp and bankdownloads tables

import requests

host='http://localhost:8080'

# Truncate bankdownloads
endpoint = '/bankdownloadstruncate'
url=host+endpoint
response = requests.delete(url)
output_data = response.json()  # Convert the response to JSON format
print(f'Truncated Table bankdownloads. Result = {output_data}')

# Truncate transactionstmp
# Execute the code below at the start of the month 
endpoint = '/transactionstmptruncate'
url=host+endpoint
response = requests.delete(url)
output_data = response.json()  # Convert the response to JSON format
print(f'Truncated Table transactionstmp. Result = {output_data}')