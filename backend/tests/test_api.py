from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get('/api/v1/health').json()['status']=='ok'
def test_math(): assert client.post('/api/v1/math/differentiate',json={'expression':'x**2'}).json()['result']=='2*x'
