# Projeto FDCA 

Este é o repositório do **Projeto FDCA**, um sistema web desenvolvido em Python utilizando o framework **Django**.

## Tecnologias Utilizadas

*   **Python 3.x**
*   **Django 5.x** 
*   **SQLite** 
*   **Python-dotenv** 

---

## Como rodar o projeto no seu computador

Como as dependências do ambiente virtual (`.venv`), as senhas (`.env`) e o banco de dados (`db.sqlite3`) estão protegidos no `.gitignore`, siga os passos abaixo para recriar o ambiente do zero.

### 1. Clonar o repositório
Abra o seu terminal e clone o projeto:
```bash
git clone https://github.com/Joao-7/FDCA.git
cd FDCA
```

### 2. Criar e Ativar o Ambiente Virtual (.venv)
Crie um ambiente isolado para não conflitar com outras versões do seu PC:

*   **Windows (PowerShell):**
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
*   **Linux / macOS:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 3. Instalar as Dependências
Com a `(.venv)` ativa no terminal, instale todos os pacotes necessários de uma só vez:
```bash
python -m pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente (.env)
1. Na raiz do projeto, você encontrará o arquivo `.env.example`.
2. Faça uma cópia dele e renomeie o novo arquivo para **`.env`**.
3. Abra o arquivo `.env` e preencha com as suas chaves locais:
   ```text
   SECRET_KEY=sua_chave_secreta_aqui
   DEBUG=True
   ```

### 5. Criar o Banco de Dados e as Tabelas
Execute as migrações para o Django criar o arquivo `db.sqlite3` e estruturar o banco de dados:
```bash
python manage.py migrate
```

### 6. Criar um Usuário Administrador (Opcional)
Para acessar o painel de controle do Django e testar o login, crie um superusuário:
```bash
python manage.py createsuperuser
```

### 7. Iniciar o Servidor
Agora é só dar o play no sistema:
```bash
python manage.py runserver
```
Abra o seu navegador e acesse: `http://127.0.0`

---

## Segurança e Repositório Público

Este repositório está configurado seguindo as boas práticas de segurança:
*   A **`SECRET_KEY`** e as configurações de **`DEBUG`** são carregadas dinamicamente via arquivo `.env`.
*   Arquivos sensíveis e pesados como `.env`, `.venv/` e `db.sqlite3` são ignorados automaticamente pelo Git e **nunca** serão expostos publicamente.

