from escape_game import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# def test_index(client):
#    response = client.get('/')
#    assert response.data == b'Flask Heroku Demo'

# def test_hello(client):
#    response = client.get('/hello')
#    assert response.data == b'Hello World!'

#

def test_index(client):
    response = client.get('/')
    assert b'Welcome to Escape The Curse Of Chucky game!' in response.data
    assert b'Enter Command:' in response.data

def test_hello(client):
    response = client.get('/hello')
    assert b'Hello, World!' in response.data
