import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server import app

import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ------------------------
# /status
# ------------------------
def test_status_endpoint(client):
    response = client.get('/status/')
    assert response.status_code == 200
    assert response.is_json
    assert response.json['status'] in ['NOT_DEPLOYED', 'PENDING', 'DEPLOYING', 'RUNNING']

# ------------------------
# /completion/
# ------------------------
def test_completion_valid_request(client):
    payload = {
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }
    response = client.post('/completion/', json=payload)
    assert response.status_code == 200
    assert response.is_json
    assert response.json['status'] == 'success'
    assert response.json['response'][0]['role'] == 'assistant'
    assert 'Echo:' in response.json['response'][0]['message']

def test_completion_invalid_request(client):
    payload = {
        "messages": [
            {"role": "assistant", "content": "Hi"}
        ]
    }
    response = client.post('/completion/', json=payload)
    assert response.status_code == 400
    assert response.is_json
    assert response.json['status'] == 'error'

# ------------------------
# /model
# ------------------------
def test_model_get(client):
    response = client.get('/model/')
    assert response.status_code == 200
    assert response.is_json
    assert 'model_id' in response.json

def test_model_post_success(client):
    # Assuming you accept this as a valid deployment request
    response = client.post('/model/')
    assert response.status_code == 200
    assert response.is_json
    assert response.json['status'] == 'success'
    assert 'model_id' in response.json

