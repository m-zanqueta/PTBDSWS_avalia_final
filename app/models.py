from . import db


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    professores = db.relationship('Professor', backref='disciplina', lazy='dynamic')


class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))