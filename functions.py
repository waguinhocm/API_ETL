import os
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("chave_api"))
url = "https://jsonplaceholder.typicode.com/posts/"


def get_user(id):
    """
        Busca os dados de um post/usuário na API.

    Args:
        id (int | str): Identificador do recurso a ser buscado.

    Returns:
        dict | None: Retorna o dicionário com os dados da resposta em caso de sucesso
        (status HTTP 200) ou None caso o recurso não seja encontrado.
    """
    response = requests.get(f'{url}{id}')
    return response.json() if response.status_code == 200 else None


def gerar_texto(user):
    """
        Gera uma mensagem motivacional personalizada usando a API da Gemini.

    Args:
        user (dict): Dicionário contendo os dados do usuário/post.
            Espera-se que contenha a chave 'nome'.

    Returns:
        str: Texto com a mensagem motivacional gerada pela IA.
    """

    chat = client.chats.create(model="gemini-3.5-flash-lite")

    pergunta = [
        "Você é um expert em bem estar emocional",
        f"Crie uma mensagem para {user['nome']} sobre em que focar no dia de hoje para um dia bem otimista e motivado",
        "a resposta deve ter o máximo 150 caracteres"
    ]

    resposta = chat.send_message(pergunta)
    return resposta.text


def update_user(user, recomends):
    """
        Atualiza o recurso do usuário na API enviando a recomendação gerada.

    Args:
        user (dict): Dicionário com as informações do usuário.
            Deve conter as chaves 'id' e opcionalmente 'userID'.
        recomends (str): O texto da recomendação que será gravado no corpo ('body') da requisição.

    Returns:
        bool: True se a requisição PUT for bem-sucedida (status 200), False caso contrário.
    """
    payload = {
        "userId": user.get('userID'),
        "id": user.get('id'),
        "title": "Recomendação de um expert!",
        "body": recomends
    }
    response = requests.put(f"{url}{user['id']}", json=payload)
    return True if response.status_code == 200 else False
