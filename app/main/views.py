from datetime import datetime
from flask import render_template, redirect, url_for, flash
from . import main
from .forms import ProfessorForm
from .. import db
from ..models import Professor, Disciplina

PERMITIDAS = ['DSWA5', 'GPSA5', 'IHCA5', 'SODA5', 'PJIA5', 'TCOA5']


@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = ProfessorForm()
    ordem = {n: i for i, n in enumerate(PERMITIDAS)}
    form.disciplina.choices = sorted(
        [(d.id, d.nome) for d in Disciplina.query.filter(Disciplina.nome.in_(PERMITIDAS))],
        key=lambda c: ordem[c[1]])
    if form.validate_on_submit():
        db.session.add(Professor(nome=form.nome.data.strip(),
                                 disciplina_id=form.disciplina.data))
        db.session.commit()
        flash('Professor cadastrado com sucesso!')
        return redirect(url_for('.professores'))
    lista = Professor.query.order_by(Professor.id).all()
    return render_template('professores.html', form=form, professores=lista)


@main.app_errorhandler(404)
def nao_disponivel(e):
    return render_template('nao_disponivel.html', current_time=datetime.utcnow()), 404


@main.app_errorhandler(500)
def erro_interno(e):
    db.session.rollback()
    return render_template('nao_disponivel.html', titulo='Erro interno do servidor',
                           current_time=datetime.utcnow()), 500