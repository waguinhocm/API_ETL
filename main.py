import pandas as pd
import requests
import json

url = "https://jsonplaceholder.typicode.com"

df = pd.read_csv('sdw2023.csv')
users_ids = df['userID'].tolist()
print(users_ids)


def get_user(id):
    response = requests.get(f'{url}/posts/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in users_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))
