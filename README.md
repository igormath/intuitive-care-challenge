# Intuitive-Care-Challenge

## Como rodar as aplicações:

A aplicação `2-data-transform` necessita da prévia execução de `1-web-scraping`, para que aquela consiga obter os dados do PDF do Anexo I.

**As aplicações deste teste foram construídas com Python 3.13.2, Pip 25.0.1., Postgresql 17.3 e Node.js v22.14.0**

### Passo a passo:
1) Clone ou faça download deste repositório:

```bash
git clone git@github.com:igormath/intuitive-care-challenge.git
```
2) Nas pastas `1-web-scraping`, `2-data-transform` e dentro da pasta "server" em `4-api`, será necessário [criar e ativar um ambiente virtual](https://dev.to/franciscojdsjr/guia-completo-para-usar-o-virtual-environment-venv-no-python-57bo).

3) Instale as dependências necessárias em cada uma dessas pastas:

```bash
pip install -r requirements.txt
```

4) Para rodar `1-web-scraping` e `2-data-transform`, basta executar o comando:

```bash
python3 main.py
```

5) Para rodar a API, renomeie o arquivo **.env-example** para **.env**, e substitua os campos **{USERNAME}**, **{PASSWORD}** e **{DATABASE_NAME}** pelos seus respectivos dados do banco de dados [Postgres](https://www.postgresql.org/download/).

6) [Crie a tabela no banco de dados com o script.sql](https://stackoverflow.com/questions/51566090/how-to-import-a-schema-sql-file-using-pgadmin-4) da pasta `3-database`

7) Inicie a aplicação:
```bash
fastapi dev ./src/main.py
```

8) Para rodar o client Vue.js, abra a pasta `4-api/client/intuitive-care` no terminal e instale as dependências necessárias:
```bash
npm install
```

9) Inicie a aplicação:
```bash
npm run dev
```

### Capturas de tela:

#### Funcionamento da interface web em Vue.js<br>
![Interface web em Vue.js](https://i.imgur.com/kb3bCZh.gif)<br>
#### Coleção com a requisição no Postman<br>
<img src="https://i.imgur.com/IL3bXN6.jpeg" alt="drawing" width="800"/>
<br>

[Imagem em maior resolução](https://i.imgur.com/IL3bXN6.jpeg)

## Referências utilizadas:
### Web Scraping:
- [Geekhunter - Como fazer web scraping python de maneira fácil e rápida](https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/)
- [StackOverflow - Download and save PDF file with Python requests module](https://stackoverflow.com/questions/34503412/download-and-save-pdf-file-with-python-requests-module)
- [StackOverflow - python zip & compress multiple files [closed]](https://stackoverflow.com/questions/47438424/python-zip-compress-multiple-files)
- [Beautiful Soup Documentation - Utilizando o find para achar uma tag em específico](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find)

### Transformação de Dados
- [Medium - Scraping de PDF usando Python](https://medium.com/@danielsantos_84603/scraping-de-pdf-usando-python-70c1dbbc92c4)
- [pdfplumber - Extracting tables](https://github.com/jsvine/pdfplumber?tab=readme-ov-file#extracting-tables)

### Banco de Dados
- [Postgresql Docs - COPY — copy data between a file and a table](https://www.postgresql.org/docs/current/sql-copy.html)
- [StackOverflow - Dockerized PGAdmin Mapped volume + COPY not working](https://stackoverflow.com/questions/68535722/dockerized-pgadmin-mapped-volume-copy-not-working)
- [Neon - PostgreSQL Change Column Type](https://neon.tech/postgresql/postgresql-tutorial/postgresql-change-column-type)

### API
- [FastAPI Best Practices - Project Structure](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#project-structure)
- [FastAPI Docs - Use CORSMiddleware](https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware)