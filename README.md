# Tic-Tac-Toe

Nesta aplicação temos como objetivo a criação de um serviço para para o famoso "jogo da velha".
O objetivo é simples através de uma request você irá começar uma partida e adquirir o ID da mesma.
Logo em seguida o jogador inicial irá fazer o movimento e depois outro jogador irá fazer o próximo movimento.
Além de ser um ótimo modo para aplicar os meus conhecimentos este projeto foi feito na linguagem PYTHON e SEM USAR BANCO DE DADOS EXTERNOS como pré-requisitos para o desenvolvimento.

**Índice**
1. [Váriaveis de ambiente](#environments)
2. [Configuração do ambiente](#cs1)
3. [Migrations](#cs2)
4. [Links](#cs3)

## Requisitos
- Python 3.x

## Informações adicionais
O arquivo `.env` serve para setar variáveis de ambiente em modo de desenvolvimento ou teste.

## Váriaveis de ambiente <a name="environments"></a>
    Váriaveis de ambientes da aplicação
|              Environment              |                 Default value                 |
|---------------------------------------|-----------------------------------------------|
| HOST                                  | 0.0.0.0                                       |
| PORT                                  | 9000                                          |
| SQLALCHEMY_DATABASE_NAME              | tic-tac-toe                                   |
| SQLALCHEMY_DATABASE_URI               | sqlite:///tic-tac-toe.db                      |
| SWAGGER_VISIBLE                       | True                                          |
| SQLALCHEMY_TRACK_MODIFICATIONS        | True                                          |
| SQLALCHEMY_ECHO                       | True                                          |
| TESTING                               | False                                         |
| FLASK_ENV                             | development                                    |

## Configuração do ambiente <a name="cs1"></a>
Instalar o Virtual Env
````bash
pip install virtualenv
````

Iniciar ambiente virtual
````bash
virtualenv venv
````

Ativar ambiente virtual
````bash
- Linux
source venv/bin/activate

- Windows
venv\Scripts\activate
````

Desativar ambiente virtual
````bash
deactivate
````

Instalar dependências
````bash
pip install -r requirements.txt
````

Setar a variável de ambiente
````bash
export FLASK_APP=app
````

Para iniciar a aplicação
````bash
python run main.py
````

Para acessar a documentação basta seguit no link disponível.
````bash
http://localhost:5000/docs
````

## Migrations <a name="cs2"></a>

##### 1- Inicializar configuração de migração
```bash
flask db init
```

##### 2- Criar a migração
```bash
flask db migrate -m "DIGITA UMA MENSAGEM CURTA"
```

##### 3- Aplicar a migração no BD
```bash
flask db upgrade
```

##### 4- Reverter a última migração aplicada
```bash
flask db downgrade
```

##### 5- Mostra qual é a migration atual no BD
```bash
flask db current
```

##### 6- Mostra o histórico de migrações
```bash
flask db history
```

##### 7- Demais comandos
```bash
flask db --help
```

## Links <a name="cs3"></a>
- [Models SQLALchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
- [Relationships](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)
- [Commit/Flush/Expire/Refresh/Merge whats the difference](https://www.michaelcho.me/article/sqlalchemy-commit-flush-expire-refresh-merge-whats-the-difference)
