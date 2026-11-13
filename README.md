# FDCA - Fila Digital do Centro de Aprendizagem

Sistema web para gerenciar a fila e a presença em atendimentos do Centro de Aprendizagem, desenvolvido como trabalho prático da disciplina **Programação para Internet** (IFRN).

---

## Descrição

O atendimento de dúvidas dos alunos no Centro de Aprendizagem costuma ser feito de forma manual: lista em papel, ordem de chegada informal e pouco registro do que foi atendido. Isso gera filas desorganizadas, falta de transparência para quem espera e nenhum histórico para o professor.

O **FDCA** propõe uma **fila digital**: o professor abre um atendimento para uma turma e disciplina, os alunos entram na fila informando sua dúvida e o professor conduz o atendimento acompanhando a ordem de chegada e o status de cada aluno.

## Objetivos

- Organizar e modernizar o atendimento aos alunos no Centro de Aprendizagem.
- Dar transparência à ordem da fila para alunos e professores.
- Registrar atendimentos e dúvidas, mantendo um histórico consultável.
- Separar as experiências de **Professor** e **Aluno** com perfis e telas próprios.
- Praticar, em equipe, o desenvolvimento web com Django e boas práticas de engenharia de software.

## Funcionalidades

> O projeto está **em desenvolvimento**. A tabela abaixo indica o que já está disponível e o que ainda não está.

| Funcionalidade | Situação |
| --- | --- |
| Cadastro de turmas e perfis (Professor / Aluno) no banco de dados | Disponível |
| Login por **matrícula e senha** | Disponível |
| Redirecionamento por perfil (grade do professor ou do aluno) | Disponível |
| Controle de acesso por perfil (`@perfil_requerido`) | Disponível |
| Painel administrativo do Django | Disponível |
| Modelagem de atendimentos e itens de fila (status, vagas, uma entrada ativa por aluno) | Disponível (modelos) |
| Entrar na fila informando a dúvida (máx. 500 caracteres) | Em desenvolvimento (formulário pronto, fluxo completo pendente) |
| Painel do professor para abrir, pausar, chamar e encerrar atendimentos | Em desenvolvimento (telas ainda sem lógica) |
| Histórico de atendimentos e detalhes | Em desenvolvimento (telas ainda sem lógica) |

## Tecnologias utilizadas

- **Python** e **Django** (padrão MVT)
- **SQLite** como banco de dados de desenvolvimento
- **python-dotenv** para variáveis de ambiente
- **HTML** para os templates
- **Git** e **GitHub** para versionamento

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) (com `pip`)
- [Git](https://git-scm.com/)
- Um terminal (PowerShell no Windows, ou bash/zsh no Linux e macOS)

## Instalação e execução

Como `.venv/`, `.env` e `db.sqlite3` estão no `.gitignore`, é preciso recriar o ambiente localmente.

### 1. Clonar o repositório

```bash
git clone https://github.com/Joao-7/FDCA.git
cd FDCA
```

### 2. Criar e ativar o ambiente virtual

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

1. Copie o arquivo `.env.example` e renomeie a cópia para `.env`.
2. Preencha com seus valores locais:
   ```text
   SECRET_KEY=sua_chave_secreta_aqui
   DEBUG=True
   ```

### 5. Entrar na pasta do projeto Django

Os comandos do Django devem ser executados na pasta que contém o `manage.py`:

```bash
cd projeto_fdca
```

### 6. Criar o banco de dados e as tabelas

```bash
python manage.py migrate
```

### 7. Criar um usuário administrador (opcional)

Útil para acessar o painel `/admin` e cadastrar turmas e perfis de teste:

```bash
python manage.py createsuperuser
```

### 8. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

## Estrutura do projeto

```text
FDCA/
├── projeto_fdca/          # Projeto Django (contém o manage.py)
│   ├── projeto_fdca/      # Configurações (settings.py, urls.py)
│   ├── conta/             # Turmas, perfis, login por matrícula e decorators de acesso
│   └── fila/              # Atendimentos, itens de fila, formulários e views
├── .env.example           # Modelo das variáveis de ambiente
├── .gitignore
├── requirements.txt       # Dependências do projeto
└── README.md
```

> Ajuste os nomes das pastas caso a estrutura do repositório seja diferente.

## Segurança

- `SECRET_KEY` e `DEBUG` são carregados via arquivo `.env`.
- Arquivos sensíveis ou locais (`.env`, `.venv/`, `db.sqlite3`) são ignorados pelo Git e não são publicados no repositório.

## Equipe

Integrantes:
|João Lucas Alves Dantas| 
|Lucas Gomes da Silva| 
|Viniciws Palhano Dantas|

Projeto desenvolvido no **IFRN** para a disciplina de **Programação para Internet**.
