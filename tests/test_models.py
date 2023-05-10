from werkzeug.security import generate_password_hash
from your_news.models import User, Article

def test_new_user():
    new_user = User(email='user@gmail.com', username='user', password=generate_password_hash('123'))

    assert new_user.email == 'user@gmail.com'
    assert new_user.password != '123'

def test_new_article():
    new_article = Article(title='Tytuł', authors='Autor',
                              url='www.test.com', media='www.img.com', user_id='1')
    
    assert new_article.title == 'Tytuł'
    assert new_article.user_id == '1'