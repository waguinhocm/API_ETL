import requests


def get_user(id):
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f'{url}/posts/{id}')
    return response.json() if response.status_code == 200 else None
