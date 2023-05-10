def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert '<h1 id="title">Current News</h1>' in response.text
    assert '<div class="article">' in response.text


def test_readlater(client):
    response = client.get('/readlater')
    assert response.status_code == 302


def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert '<input class="btn btn-primary mt-2" type="submit" value="Log in">' in response.text


def test_register(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert '<input class="btn btn-primary mt-2" type="submit" value="Register">' in response.text
