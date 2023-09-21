# 📚 Traduzo

Neste projeto, desenvolvi uma aplicação full stack que clona o google tradutor! De acordo com a arquitetura MVC (Model, View, Controller), é possível cadastrar a consultar idiomas, consultar o histórico de traduções e fazer tradução reversa. A estilização foi fornecida pela escola de programação Trybe.

![front-end](https://github.com/bermartorano/traduzo/assets/110858573/b23d5aa9-14a7-49d3-be9e-4cc33d171ac1)

## 🛠️ Ferramentas Utilizadas
* Python
* MongoDB
* PyMongo
* Flask
* Docker

## 🖱️ Como Executar a Aplicação
1. Clone o repositório.
2. Na raiz do projeto, crie e entre no ambiente virtual `python3 -m venv .venv && source .venv/bin/activate`.
3. Instale as dependências `python3 -m pip install -r dev-requirements.txt`.
4. Suba o projeto com o Docker `docker compose up translate`.
5. Utilize o comando `docker compose exec -it translate python3 src/run_seeds.py` para popular o banco.
6. A aplicação pode ser acessada pelo navegador com a rota http://127.0.0.1:8000/

## Detalhes da Implementação
![requisitor-01](https://github.com/bermartorano/traduzo/assets/110858573/52c875e2-36bf-4db2-a933-e365e48dc779)
![requisitos-02](https://github.com/bermartorano/traduzo/assets/110858573/477b47bb-6780-47a5-bb23-ec9d4523cb00)
