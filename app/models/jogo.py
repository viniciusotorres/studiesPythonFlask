from .. import db

class Jogo(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    console = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Jogo {self.nome}>'