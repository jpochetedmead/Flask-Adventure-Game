#import escape_game

#def test_import():
#    assert escape_game

from flaskherokudemo import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'Flask Heroku Demo'
