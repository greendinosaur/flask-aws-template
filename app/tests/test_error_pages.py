

def test_403_forbidden(test_client):
    response = test_client.get('/403')
    assert response.status_code == 403


def test_404_not_found(test_client):
    response = test_client.get('/nothinghere')
    assert response.status_code == 404


def test_500_internal_server_error(test_client):
    response = test_client.get('/500')
    assert response.status_code == 500


def test_general_server_error(test_client):
    response = test_client.get('/general_exception')
    assert response.status_code == 500
