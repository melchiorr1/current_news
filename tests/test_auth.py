from your_news.models import User
from flask_login import current_user, AnonymousUserMixin


def test_register(client, app):
    client.post('/register', data={
        'username': 'Mikołaj',
        'email': 'miko@gmail.com',
        'password': '123',
        'repeat_password': '123'
    })
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.filter_by(username='Mikołaj').first() is not None
        assert User.query.filter_by(
            username='Mikołaj').first().email == 'miko@gmail.com'


def test_register_passwords_do_not_match(client, app):
    client.post('/register', data={
        'username': 'Mikołaj',
        'email': 'miko@gmail.com',
        'password': '321',
        'repeat_password': '123'
    })
    with app.app_context():
        assert User.query.count() == 0
        assert User.query.filter_by(username='Mikołaj').first() is None

def test_login_correct(client):
    with client:
        client.post('/register', data={
            'username': 'Mikołaj',
            'email': 'miko@gmail.com',
            'password': '123',
            'repeat_password': '123'
        })
        client.post('/login', data={
            'email': 'miko@gmail.com',
            'password': '123'
        })

        assert current_user.username == "Mikołaj"
        assert current_user.email == "miko@gmail.com"

def test_login_wrong_password(client):
    with client:
        client.post('/register', data={
            'username': 'Mikołaj',
            'email': 'miko@gmail.com',
            'password': '123',
            'repeat_password': '123'
        })

        client.get('/logout')
        client.post('/login', data={
            'email': 'miko@gmail.com',
            'password': '1234'
        })

        assert current_user.get_id() is None

