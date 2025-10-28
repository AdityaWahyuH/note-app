import pytest
from app import app, notes

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    # Cleanup notes after each test
    notes.clear()

def test_index_page(client):
    """Test halaman utama dapat diakses"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Notes' in response.data

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
    assert 'notes_count' in json_data

def test_add_note(client):
    """Test menambahkan note baru"""
    response = client.post('/add', data={'title': 'Test Note'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Note' in response.data

def test_new_note_page(client):
    """Test halaman form tambah note"""
    response = client.get('/new')
    assert response.status_code == 200
    assert b'Note Title' in response.data

def test_multiple_notes(client):
    """Test menambahkan beberapa notes"""
    client.post('/add', data={'title': 'Note 1'})
    client.post('/add', data={'title': 'Note 2'})
    
    response = client.get('/health')
    json_data = response.get_json()
    assert json_data['notes_count'] == 2
