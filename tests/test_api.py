from lab.api.app import create_app

def test_status_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.get('/api/status')
    assert resp.status_code == 200
