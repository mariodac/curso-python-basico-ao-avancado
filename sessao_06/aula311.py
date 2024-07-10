# requests para requisições HTTP
import requests
from pprint import pprint
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes
from os import path
# http:// -> 80
# https:// -> 443
# python -m http.server -d ./ 3333 
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
print(response.headers)
# print(response.text)

# Requests em Python - Consumindo uma API Rest usando o módulo Requests - Aula do youtube https://www.youtube.com/watch?v=Qd8JT0bnJGs

def show_info(response):
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    print('JSON: ')
    pprint(response.json())
    

def create_user(user:str, password:str, email:str):
    # criar usuario
    url = 'http://localhost:3001/users/'

    user_data = {
        "nome": user,
        "password": password,
        "email": email
    }

    response = requests.post(url, json=user_data)

    if response.status_code >= 200 and response.status_code <= 299:
        show_info(response)
    else:
        show_info(response)
    


def create_token(email, password):
    url = 'http://localhost:3001/tokens/'

    user_data = {
        "password": password,
        "email": email,
    }

    response = requests.post(url, json=user_data)

    show_info(response)
    if response.status_code >= 200 and response.status_code <= 299:
        response_data = response.json()
        token = response_data['token']
        with open('_token.txt', 'w') as file_txt:
            file_txt.write(token)
        show_info(response)
    else:
        show_info(response)


def get_token():
    token = 'Bearer '

    with open('_token.txt', 'r') as file_txt:
        token += file_txt.read()

    return token

def create_aluno(nome, sobrenome, email, idade, peso, altura):
    url = 'http://localhost:3001/alunos/'
    aluno_data = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "idade": idade,
        "peso": peso,
        "altura": altura
    
    }

    token = get_token()
    
    headers = {
        'Authorization': token
    }

    response = requests.post(url, json=aluno_data, headers=headers)

    if response.status_code >= 200 and response.status_code <= 299:
        show_info(response)
    else:
        show_info(response)

def get_aluno(id_aluno):
    url = f'http://localhost:3001/alunos/{id_aluno}'

    response = requests.get(url)
    show_info(response)

def get_alunos():
    url = f'http://localhost:3001/alunos/'

    response = requests.get(url)
    
    for aluno in response.json():
        pprint(aluno)

def put_alunos(id_aluno, nome, sobrenome, email, idade, peso, altura):
    url = f'http://localhost:3001/alunos/{id_aluno}'

    aluno_data = {
        "nome": nome,
        # "sobrenome": sobrenome,
        # "email": email,
        # "idade": idade,
        # "peso": peso,
        # "altura": altura
    
    }

    token = get_token()
    
    headers = {
        'Authorization': token
    }

    response = requests.put(url, json=aluno_data, headers=headers)

    if response.status_code >= 200 and response.status_code <= 299:
        show_info(response)
    else:
        show_info(response)

def delete_aluno(id_aluno):
    url = f'http://localhost:3001/alunos/{id_aluno}'

    token = get_token()
    
    headers = {
        'Authorization': token
    }

    response = requests.delete(url, headers=headers)

    if response.status_code >= 200 and response.status_code <= 299:
        show_info(response)
    else:
        show_info(response)

def upload_foto(caminho_arquivo, id_aluno):
    url = 'http://localhost:3001/fotos'
    
    mimetype = MimeTypes()
    mimetype_arquivo = mimetype.guess_type(caminho_arquivo)[0]

    # print(mimetype_arquivo)
    
    multipart = MultipartEncoder(fields={
        "aluno_id": id_aluno,
        "foto": (path.basename(caminho_arquivo), open(caminho_arquivo, 'rb'), mimetype_arquivo),
        })

    token = get_token()
    headers = {
        'Authorization': token,
        'Content-Type': multipart.content_type
    }

    response = requests.post(url, headers=headers, data=multipart)

    if response.status_code >= 200 and response.status_code <= 299:
        show_info(response)
    else:
        show_info(response)

def download_foto(url):
    nome_arquivo = '_' + url.split('/')[-1]

    response = requests.get(url)

    if response.status_code >= 200 and response.status_code <= 299:
        with open(nome_arquivo, 'wb') as file_imagem:
            file_imagem.write(response.content)
    else:
        show_info(response)
    

if __name__ == '__main__':
    ...
    # create_user('didi', 'paonoceu', 'didimoco@superemail.com')
    # create_token('didimoco@superemail.com', 'paonoceu')
    # create_aluno("juliana", "Moraes", "juliana@email.com", "50", "80.04", "1.90")
    # get_aluno(1)
    # get_alunos()
    # put_alunos(1, 'Guilherme', 'Santana', 'guilherme@email.com', '51', '80.14', '1.91')
    # get_alunos()
    # delete_alunos(1)
    # caminho_imagem = Path(__file__).parent / '_log_python.jpg'
    # caminho_imagem = path.join(path.dirname(__file__), '_log_python.jpg') 
    # upload_foto(caminho_imagem, '3')
    # get_alunos()
    download_foto('http://localhost:3001/images/1720600605551_13838.jpg')

