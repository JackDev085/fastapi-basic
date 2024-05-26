# Projeto básico Webservice para treinos

1. **Configuração do Ambiente Virtual:**
   - Primeiramente, entre em um ambiente virtual de sua preferência. Você pode fazer isso utilizando um dos seguintes comandos:
     ```shell
     python -m venv venv
     ```
     ou
     ```shell
     python3 -m venv venv
     ```

2. **Instalação das Dependências:**
   - Antes de prosseguir, é importante instalar as dependências do projeto. Você pode fazer isso utilizando o comando:
     ```shell
     pip install -r requirements.txt
     ```

3. **Criação do Banco de Dados:**
   - Em seguida, execute o arquivo `makedb.py` para criar um banco de dados localmente nos arquivos. O banco de dados será criado em `./infra/configs/teste.db`. Utilize o seguinte comando:
     ```shell
     python makedb.py
     ```

5. **Inicialização do Servidor FastAPI:**
   - Após iniciar a aplicação, execute o seguinte comando para iniciar o servidor FastAPI:
     ```shell
     uvicorn run:app --reload
     ```

6. **Acesso à Interface da Aplicação:**
   - Uma vez que o servidor esteja em execução, você pode acessar a tela inicial da aplicação digitando o seguinte URL em seu navegador:
     [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

7. **Acesso à Documentação da API:**
   - Para analisar a documentação da API e entender como a aplicação funciona, acesse o seguinte URL:
     [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
