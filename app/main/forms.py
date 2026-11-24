from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ProfessorForm(FlaskForm):
    nome = StringField('Cadastre o novo Professor:', validators=[DataRequired()])
    disciplina = SelectField('Disciplina associada:', coerce=int)
    submit = SubmitField('Cadastrar')