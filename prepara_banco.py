import mysql.connector
from mysql.connector import errorcode

try:
    # Conectar ao banco de dados MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345'
    )
    print("Conexão ao MySQL estabelecida com sucesso.")

    cursor = conn.cursor()

    # Criar o banco de dados jogoteca se não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS jogoteca")
    print("Banco de dados 'jogoteca' verificado/criado com sucesso.")
    cursor.execute("USE jogoteca")

    # Criar a tabela de jogos se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        console VARCHAR(50) NOT NULL
    )
    """)
    print("Tabela 'jogos' verificada/criada com sucesso.")

    # Criar a tabela de usuários se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario VARCHAR(50) NOT NULL,
        senha VARCHAR(100) NOT NULL
    )
    """)
    print("Tabela 'usuarios' verificada/criada com sucesso.")

    # Inserir dados iniciais na tabela de usuários
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', '12345')")
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('aluno', '123')")
    print("Dados iniciais inseridos na tabela 'usuarios'.")

    # Confirmar as alterações
    conn.commit()
    print("Alterações confirmadas com sucesso.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro de acesso: Verifique o usuário e a senha.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro de banco de dados: O banco de dados não existe.")
    else:
        print(err)
