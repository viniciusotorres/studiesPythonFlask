class Config:
    SECRET_KEY = 'alura'
    SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql',
        usuario='root',
        senha='12345',
        servidor='localhost',
        database='jogoteca'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False