import functions as fc
import os
import pandas as pd
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("chave_api"))

df = pd.read_csv('sdw2023.csv')
users_ids = df['userID'].tolist()
print(users_ids)


users = [user for id in users_ids if (user := fc.get_user(id)) is not None]
print(json.dumps(users, indent=2))

chat = client.chats.create(model="gemini-3.5-flash-lite")

print("--- Chat com Gemini Iniciado (digite 'sair' para encerrar) ---")

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("Chat encerrado!")
        break

    resposta = chat.send_message(pergunta)
    print(f"\nGemini: {resposta.text}")
