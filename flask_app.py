from app import create_app, db
from app.models import Disciplina

app = create_app()

DISCIPLINAS = [
    ('DSWA5', 5), ('PTBPBD', 5), ('TCOA5', 5), ('IHCA5', 5), ('PTBDSWS', 4),
    ('GPSA5', 5), ('Redes', 1), ('SODA5', 5), ('Matemática', 4), ('portugues', 6),
]

with app.app_context():
    db.create_all()
    if Disciplina.query.count() == 0:
        db.session.add_all([Disciplina(nome=n, semestre=s) for n, s in DISCIPLINAS])
        db.session.commit()