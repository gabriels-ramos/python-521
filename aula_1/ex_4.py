import requests
URL = 'https://gen-net.herokuapp.com/api/users/{}'
NUSER = input('Numero do usuario: ')
response = requests.get(URL.format(NUSER))
print(response.json())