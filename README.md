# Tic-Tac-Toe

Nesta aplicação temos como objetivo a criação de um serviço para para o famoso "jogo da velha".
O objetivo é simples através de uma request você irá começar uma partida e adquirir o ID da mesma.
Logo em seguida o jogador inicial irá fazer o movimento e depois outro jogador irá fazer o próximo movimento.
Além de ser um ótimo modo para aplicar os meus conhecimentos este projeto foi feito na linguagem PYTHON e SEM USAR BANCO DE DADOS EXTERNOS como pré-requisitos para o desenvolvimento.

**Índice**
1. [Váriaveis de ambiente](#environments_variables)
2. [Configuração do ambiente](#environment)
3. [Migrations](#migration)
4. [Testes unitários](#coverage)
5. [Links](#links)

## Requisitos
- Python 3.x

## Informações adicionais
O arquivo `.env` serve para setar variáveis de ambiente em modo de desenvolvimento.

## Váriaveis de ambiente <a name="environments_variables"></a>
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
| FLASK_ENV                             | development                                   |
| DEBUG                                 | False                                         |

## Configuração do ambiente <a name="environment"></a>
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
flask run
````

Para acessar a documentação basta seguit no link disponível.
````bash
http://localhost:5000/docs
````

## Migrations <a name="migration"></a>

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
## Testes unitários com Coverage <a name="coverage"></a>
O [Coverage](https://coverage.readthedocs.io/en/coverage-5.0/) é uma ferramenta para medir a cobertura de código de programas em Python. Ele monitora seu programa, observando quais partes do código foram executadas, em seguida, analisa a fonte para identificar o código que poderia ter sido executado, mas não foi.

Instalar dependência
````bash
pip install coverage
````

Para executar os testes rode os comandos abaixo
````bash
coverage run -m nose -v
````

Para gerar um relatório de seus testes execute 
````bash
coverage report -m
````

Para verificar os detalhes de seu código você pode gerar um html dos relatórios e analisar individualmente cada parte de seu código. Para isso basta rodar o comando abaixo 
````bash
coverage html
````

## Links <a name="links"></a>
- [Models SQLALchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
- [Relationships](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)
- [Commit/Flush/Expire/Refresh/Merge whats the difference](https://www.michaelcho.me/article/sqlalchemy-commit-flush-expire-refresh-merge-whats-the-difference)
