from .. import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.usuario}>'