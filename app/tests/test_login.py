from unittest.mock import patch

@patch('app.oauth')
def test_login(mock_auth0, test_client, init_database):
    mock_auth0.auth0.authorize_redirect.return_value = 200

    response = test_client.get('/auth/authorize')
    assert response.status_code == 302
