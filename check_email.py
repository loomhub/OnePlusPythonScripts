import requests
host='http://localhost:8080'

# Bank Downloads
endpoint='/bankdownloads/email?'
receiver= 'receiver=vivekjadhav@yahoo.com'
keyword='&keyword=Bank Downloads'
url=host+endpoint+receiver+keyword

data = requests.get(url).json()
print(data)