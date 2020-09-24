import glob
import os

from unittest.mock import patch

from app.models import User
from app.tests import conftest


def delete_test_file():
    files = glob.glob("*bobby.json")
    os.remove(files[0])


def test_contact_us_logged_in_user(test_client_csrf, init_database):
    u = User.query.filter_by(username=conftest.TEST_USER_USERNAME).first()

    with patch('flask_login.utils._get_user') as current_user:
        current_user.return_value.id = u.id
        current_user.return_value.get_id.return_value = u.id
        params = dict(
            name="Bobby Chariot",
            email="bobby@chariot.email",
            subject="Feedback",
            message="Hello to you all",
            csrf_token=test_client_csrf.csrf_token)

        response = test_client_csrf.post('/support/contact_us', data=params)

        assert response.status_code == 302
        # then delete the file
        delete_test_file()



def test_contact_us_anon(test_client_csrf):
    params = dict(
        name="Bobby Chariot",
        email="bobby@chariot.email",
        subject="Feedback",
        message="Hello to you all",
        csrf_token=test_client_csrf.csrf_token)

    response = test_client_csrf.post('/support/contact_us', data=params)

    assert response.status_code == 302
    delete_test_file()


def test_contact_us_missing_email(test_client_csrf):
    params = dict(
        name="Bobby Chariot",
        email="",
        subject="Feedback",
        message="Hello to you all",
        csrf_token=test_client_csrf.csrf_token)

    response = test_client_csrf.post('/support/contact_us', data=params)

    assert response.status_code == 200
    assert "This field is required" in str(response.data)


def test_contact_us_missing_name(test_client_csrf):
    params = dict(
        name="",
        email="bobby@chariot.email",
        subject="Feedback",
        message="Hello to you all",
        csrf_token=test_client_csrf.csrf_token)

    response = test_client_csrf.post('/support/contact_us', data=params)

    assert response.status_code == 200
    assert "This field is required" in str(response.data)


def test_contact_us_missing_message(test_client_csrf):
    params = dict(
        name="Bobby Chariot",
        email="bobby@chariot.email",
        subject="Feedback",
        message="",
        csrf_token=test_client_csrf.csrf_token)

    response = test_client_csrf.post('/support/contact_us', data=params)

    assert response.status_code == 200
    assert "This field is required" in str(response.data)


def test_contact_us_missing_subject(test_client_csrf):
    params = dict(
        name="Bobby Chariot",
        email="bobby@chariot.email",
        subject="",
        message="Hello to you all",
        csrf_token=test_client_csrf.csrf_token)

    response = test_client_csrf.post('/support/contact_us', data=params)

    assert response.status_code == 200
    assert "This field is required" in str(response.data)
