import json
import logging
import pandas as pd
import functions as fc


def main():

    try:
        df = pd.read_csv('lista_id_alterar.csv')
    except FileNotFoundError:
        logging.error("Arquivo não encontrado.")
        return

    users = []

    for _, row in df.iterrows():
        user_id = row["userID"]
        nome = row["nome"]
        dados = fc.get_user(row['userID'])

        if dados:
            dados['nome'] = nome
            users.append(dados)

        else:
            logging.warning(f"Usuário id {user_id} não encontrado na API")

    for user in users:
        try:
            recomends = fc.gerar_texto(user)

            succes = fc.update_user(user, recomends)
            if succes:
                user['title'] = "Recomendação de um expert!"
                user['body'] = recomends
                print(json.dumps(user, indent=2, ensure_ascii=False))
            else:
                logging.error(f"Falha ao atualizar o usuário {user['id']} ({user['nome']}) na API.")

        except Exception as e:
            logging.error(f"Erro ao processar o usuário {user.get('id')}: {e}")


if __name__ == "__main__":
    main()
