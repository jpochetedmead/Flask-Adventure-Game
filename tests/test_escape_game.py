from escape_game import *

def test_import():
    assert create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'In this game your goal is to escape from Chucky, or at least survive as long as you can. Have fun!' in response.data

def test_hello(client):
    response = client.get('/hello')
    assert b'Hello, World!' in response.data

####################################
######### TESTING FOR PRACTICE
#def test_greeting_page(client):
#    response1 = client.get('/greet/Amy')
#    assert b'Hello Amy' in response1.data

#    response2 = client.get('/greet/Bob')
#    assert b'Hello Amy' not in response2.data
#    assert b'Hello Bob' in response2.data
