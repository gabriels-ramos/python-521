import requests
DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/'

payload = {
'name': input('Digite seu nome: '),
'email': input('Digite seu email: '),
'password': input('Digite sua senha: ')
}

res = requests.post(DOMAIN_URL, payload)

if res.status_code == 200:
    print("Usuario cadastrado com sucesso")
else:
    print("Email ja cadastrato")
