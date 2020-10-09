def test_homepage_view(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_welcome_view(test_client):
    response = test_client.get('/welcome')
    assert response.status_code == 200


def test_index_view(test_client):
    response = test_client.get('/index')
    assert response.status_code == 302


def test_login_view(test_client):
    response = test_client.get('/auth/login')
    assert response.status_code == 200


def test_logout_view(test_client):
    response = test_client.get('/auth/logout')
    assert response.status_code == 302


def test_logout_new_view(test_client):
    response = test_client.get('/auth/logout_new')
    assert response.status_code == 302


def test_view_profile_view(test_client):
    response = test_client.get('/user')
    assert response.status_code == 302


def test_view_service_worker(test_client):
    response = test_client.get('service-worker.js')
    assert response.status_code == 200


def test_view_privacy(test_client):
    response = test_client.get('/support/privacy')
    assert response.status_code == 200


def test_view_disclaimer(test_client):
    response = test_client.get('/support/disclaimer')
    assert response.status_code == 200


def test_view_cookies(test_client):
    response = test_client.get('/support/cookies')
    assert response.status_code == 200


def test_view_faq(test_client):
    response = test_client.get('/support/faq')
    assert response.status_code == 200


def test_view_contact_us(test_client):
    response = test_client.get('/support/contact_us')
    assert response.status_code == 200


def test_view_about(test_client):
    response = test_client.get('/about')
    assert response.status_code == 200


def test_view_sitemap(test_client):
    response = test_client.get('/sitemap.xml')
    assert response.status_code == 200


def test_view_robot(test_client):
    response = test_client.get('/robots.txt')
    assert response.status_code == 200
