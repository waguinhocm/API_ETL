# 🚀 ETL Pipeline: Mensagens Personalizadas de Bem-Estar com Gemini AI

Este é um projeto de **ETL (Extract, Transform, Load)** em Python que consome dados de usuários a partir de um arquivo CSV e de uma API REST, gera recomendações diárias de bem-estar utilizando a **API da Google Gemini AI** e envia as atualizações de volta para o servidor.

---

## 📌 Funcionalidades

- **Extract (Extração):** Lê a lista de IDs e nomes a partir de um arquivo CSV local (`lista_id_alterar.csv`) e busca informações complementares na API REST (`JSONPlaceholder`).
- **Transform (Transformação):** Utiliza o modelo **Gemini 3.5 Flash Lite** da Google para criar mensagens motivacionais personalizadas e curtas (máximo 150 caracteres) para cada usuário.
- **Load (Carregamento):** Atualiza os dados do usuário na API externa (`PUT`) com o conteúdo gerado pela IA.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** (para leitura e manipulação do CSV)
- **Requests** (para integração HTTP com APIs REST)
- **google-genai** (SDK oficial da Google para integração com modelos Gemini)
- **python-dotenv** (gerenciamento seguro de variáveis de ambiente)

---

## 📂 Estrutura do Projeto

```text
api_etl/
│── main.py                 # Fluxo principal do pipeline ETL
│── functions.py            # Módulo com as funções de requisição e chamada à IA
│── lista_id_alterar.csv    # Arquivo de entrada com os dados dos usuários
│── requirements.txt        # Dependências do projeto
│── .env                    # Variáveis de ambiente (não versionado no Git)
└── README.md               # Documentação do projeto