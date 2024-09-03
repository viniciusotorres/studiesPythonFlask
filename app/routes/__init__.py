from flask import Blueprint

jogo_bp = Blueprint('jogo', __name__)
usuario_bp = Blueprint('usuario', __name__)

from . import jogo, usuario