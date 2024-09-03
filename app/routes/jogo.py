from flask import render_template, request, redirect, session, flash, url_for
from . import jogo_bp
from ..models import Jogo
from .. import db


@jogo_bp.route('/')
def index():
    lista = Jogo.query.order_by(Jogo.id).all()
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)

@jogo_bp.route('/novo-jogo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('usuario.login', proxima='novo-jogo'))
    return render_template('novo-jogo.html', titulo='Novo Jogo')

@jogo_bp.route('/criar', methods=['POST'])
def criar():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Você precisa estar logado para criar um novo jogo!')
        return redirect(url_for('usuario.login'))

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo.query.filter_by(nome=nome).first()

    if jogo:
        flash(f'O jogo {jogo.nome} já existe!')
        return redirect(url_for('jogo.index'))
    else:
        jogo = Jogo(nome=nome, categoria=categoria, console=console)
        db.session.add(jogo)
        db.session.commit()

    return redirect(url_for('jogo.index'))