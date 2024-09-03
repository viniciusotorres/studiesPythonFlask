from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Cria uma instância do Flask com o nome do módulo atual (__name__)
app.secret_key = 'alura'  # Define uma chave secreta para a aplicação

# Configuração do banco de dados com SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql',
        usuario = 'root',
        senha = '12345',
        servidor = 'localhost',
        database = 'jogoteca'
    )  # Define a URI do banco de dados \\ URI = Uniform Resource Identifier (Identificador de Recurso Uniforme)

db = SQLAlchemy(app)  # Cria uma instância do SQLAlchemy(ORM) com a instância do Flask

class Jogo(db.Model): # Cria uma classe Jogo que herda de db.Model
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True) # Cria um campo id do tipo inteiro e chave primária
    nome = db.Column(db.String(255), nullable=False) # Cria um campo nome do tipo string com no máximo 255 caracteres e não nulo
    categoria = db.Column(db.String(255), nullable=False) # Cria um campo categoria do tipo string com no máximo 255 caracteres e não nulo
    console = db.Column(db.String(255), nullable=False) # Cria um campo console do tipo string com no máximo 255 caracteres e não nulo

    def __repr__(self): # Metodo para representar a classe como uma string
        return f'<Jogo {self.nome}>'

class Usuario(db.Model): # Cria uma classe Usuario que herda de db.Model
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True) # Cria um campo id do tipo inteiro e chave primária
    usuario = db.Column(db.String(255), nullable=False) # Cria um campo usuario do tipo string com no máximo 255 caracteres e não nulo
    senha = db.Column(db.String(255), nullable=False) # Cria um campo senha do tipo string com no máximo 255 caracteres e não nulo

    def __repr__(self): # Metodo para representar a classe como uma string
        return f'<Usuario {self.usuario}>'

############################
#### PÁGINA INICIAL #########
############################
@app.route('/')
def index():
    lista = Jogo.query.order_by(Jogo.id).all()
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)
    # Renderiza o template lista.html com o título da página passado como parâmetro

############################
#### PÁGINA DE NOVO JOGO ####
############################
@app.route('/novo-jogo')
def novo():  # Função para criar um novo jogo
    if 'usuario_logado' not in session or session['usuario_logado'] is None:  # Verifica se o usuário está logado
        return redirect(url_for('login', proxima='novo-jogo'))  # Redireciona para a página de login

    return render_template('novo-jogo.html', titulo='Novo Jogo')
    # Renderiza o template novo-jogo.html com o título da página passado como parâmetro

############################
#### PÁGINA DE LOGIN #######
############################
@app.route('/login')
def login():
    proxima = request.args.get('proxima', '/')  # Recupera o parâmetro proxima da URL, ou '/' se não existir
    print(proxima)
    return render_template('login.html', titulo='Login', proxima=proxima)
    # Renderiza o template login.html com o título da página passado como parâmetro

############################
#### CRIAR UM NOVO JOGO ####
############################
@app.route('/criar', methods=['POST'])
def criar():  # Função para criar um novo jogo
    if 'usuario_logado' not in session or session['usuario_logado'] is None:  # Verifica se o usuário está logado
        flash('Você precisa estar logado para criar um novo jogo!')  # Exibe uma mensagem na tela
        return redirect(url_for('login'))  # Redireciona para a página de login

    nome = request.form['nome']  # Recupera o nome do jogo informado no formulário
    categoria = request.form['categoria']  # Recupera a categoria do jogo informada no formulário
    console = request.form['console']  # Recupera o console do jogo informado no formulário

    jogo = Jogo.query.filter_by(nome=nome).first()  # Busca o jogo no banco de dados

    if jogo:
        flash(f'O jogo {jogo.nome} já existe!')
        return redirect(url_for('index'))

    else:
        jogo = Jogo(nome=nome, categoria=categoria, console=console) # Cria um novo jogo com os dados informados no formulário
        db.session.add(jogo)  # Adiciona o novo jogo ao banco de dados
        db.session.commit() # Salva as alterações no banco de dados


    return redirect(url_for('index'))  # Redireciona para a página inicial

############################
#### AUTENTICAR USUÁRIO ####
############################
@app.route('/autenticar', methods=['POST'])
@app.route('/autenticar', methods=['POST'])
def autenticar():  # Função para autenticar o usuário
    usuario = Usuario.query.filter_by(usuario=request.form['usuario'], senha=request.form['senha']).first() # Busca o usuário no banco de dados

    if usuario:  # Se o usuário foi encontrado
        session['usuario_logado'] = usuario.usuario  # Define o usuário como logado
        flash(f'{usuario.usuario} logou com sucesso!')
        proxima_pagina = request.form.get('proxima', url_for('index'))
        return redirect(proxima_pagina)
    else:  # Se o usuário não foi encontrado
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


############################
#### DESLOGAR USUÁRIO ######
############################
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('index'))

############################
#### EXECUTAR O FLASK ######
############################
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor web