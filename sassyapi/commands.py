import click
from flask.cli import with_appcontext

from .extensions import guard, db
from .models import User

@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()


@click.command(name='create_users')
@with_appcontext
def create_users():
    jeden = User(email="kean@gmail.com", username='Keanu0', password=guard.hash_password('passypie123'))
    dwa = User(email="cara@gmail.com", username='Carakaka', password=guard.hash_password('passypie123'))
    trzy = User(email="fizzet@gmail.com", username='Fizzet', password=guard.hash_password('passypie123'))

    db.session.add_all([jeden, dwa, trzy])
    db.session.commit()

