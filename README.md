# Jogoteca

Jogoteca é uma aplicação web simples para gerenciar uma lista de jogos. Este projeto foi desenvolvido com fins de estudo e utiliza o framework Flask.

## Requisitos

- Python 3.x
- Flask

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/jogoteca.git
    cd jogoteca
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install flask
    ```

## Execução

1. Execute a aplicação:
    ```bash
    python jogoteca.py
    ```

2. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000/
    ```

## Uso

### Página Inicial

A página inicial exibe a lista de jogos cadastrados.

### Novo Jogo

Para adicionar um novo jogo, acesse a página `Novo Jogo`. Se você não estiver logado, será redirecionado para a página de login.

### Login

A página de login permite que você se autentique. Use as seguintes credenciais para teste:
- Usuário: `admin`
- Senha: `12345`

### Estrutura do Projeto

- `jogoteca.py`: Arquivo principal da aplicação.
- `templates/`: Diretório contendo os templates HTML.
  - `template.html`: Template base.
  - `lista.html`: Template da página inicial.
  - `login.html`: Template da página de login.
  - `novo-jogo.html`: Template da página de novo jogo.
- `static/`: Diretório para arquivos estáticos (ex.: CSS, JS).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.
