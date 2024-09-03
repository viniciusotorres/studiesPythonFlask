from flask import render_template, request, redirect, session, flash, url_for
from . import usuario_bp
from ..models import Usuario

@usuario_bp.route('/login')
def login():
    proxima = request.args.get('proxima', '/')
    return render_template('login.html', titulo='Login', proxima=proxima)

@usuario_bp.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuario.query.filter_by(usuario=request.form['usuario'], senha=request.form['senha']).first()

    if usuario:
        session['usuario_logado'] = usuario.usuario
        flash(f'{usuario.usuario} logou com sucesso!')
        proxima_pagina = request.form.get('proxima', url_for('jogo.index'))
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('usuario.login'))

@usuario_bp.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('jogo.index'))