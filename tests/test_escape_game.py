from escape_game import create_app

def test_import():
    assert create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'In this game your goal is to escape from Chucky, or at least survive as long as you can. Have fun!' in response.data
    assert b'<input type="submit"' in response.data


def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_menu(client):
    response = client.get('/menu/<name>')
    assert response.status_code == 200
    #assert b'<p>{{ person }}, please choose a menu option to proceed:</p>' in response.data

def test_guide(client):
    response = client.get('/guide')
    assert response.status_code == 200

def test_profile(client):
    response = client.get('/profile')
    assert response.status_code == 200

def test_room(client):
    response = client.get('/room')
    assert response.status_code == 200

def test_room1(client):
    response = client.get('/room1')
    assert response.status_code == 200

def test_room2(client):
    response = client.get('/room2')
    assert response.status_code == 200

def test_room3(client):
    response = client.get('/room3')
    assert response.status_code == 200

def test_room4(client):
    response = client.get('/room4')
    assert response.status_code == 200

def test_room5(client):
    response = client.get('/room5')
    assert response.status_code == 200

# Need to fix these tests below:
#def test_register(client):
#    response = client.get('/register')
#    assert response.status_code == 200

#def test_login(client):
#    response = client.get('/login')
#    assert response.status_code == 200
