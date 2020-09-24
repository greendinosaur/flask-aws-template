import flask
import pytest
from flask import abort
from flask.testing import FlaskClient as BaseFlaskClient
from flask_wtf.csrf import generate_csrf

from app import create_app, db
from app.models import User

# define some test data to be used in tests
TEST_USER_USERNAME = 'test_user'
TEST_USER_PASSWORD = 'test_password'
TEST_USER_EMAIL = 'test@test.com'

class RequestShim():
    """
    A fake request that proxies cookie-related methods to a Flask test client.
    """

    def __init__(self, client):
        self.vary = set({})
        self.client = client

    def set_cookie(self, key, value='', *args, **kwargs):
        "Set the cookie on the Flask test client."
        server_name = flask.current_app.config["SERVER_NAME"] or "localhost"
        return self.client.set_cookie(
            server_name, key=key, value=value, *args, **kwargs
        )

    def delete_cookie(self, key, *args, **kwargs):
        "Delete the cookie on the Flask test client."
        server_name = flask.current_app.config["SERVER_NAME"] or "localhost"
        return self.client.delete_cookie(
            server_name, key=key, *args, **kwargs
        )


# We're going to extend Flask's built-in test client class, so that it knows
# how to look up CSRF tokens for you!
class FlaskClient(BaseFlaskClient):
    @property
    def csrf_token(self):
        # First, we'll wrap our request shim around the test client, so that
        # it will work correctly when Flask asks it to set a cookie.
        request = RequestShim(self)
        # Next, we need to look up any cookies that might already exist on
        # this test client, such as the secure cookie that powers `flask.session`,
        # and make a test request context that has those cookies in it.
        environ_overrides = {}
        self.cookie_jar.inject_wsgi(environ_overrides)
        with flask.current_app.test_request_context(
                "/login", environ_overrides=environ_overrides,
        ):
            # Now, we call Flask-WTF's method of generating a CSRF token...
            csrf_token = generate_csrf()
            # ...which also sets a value in `flask.session`, so we need to
            # ask Flask to save that value to the cookie jar in the test
            # client. This is where we actually use that request shim we made!
            flask.current_app.save_session(flask.session, request)
            # And finally, return that CSRF token we got from Flask-WTF.
            return csrf_token


@pytest.fixture(scope='module')
def test_client():
    """
    sets up a client to use in the tests
    :return:
    :rtype:
    """
    testing_app = create_app('testing')

    # set-up some error routes
    @testing_app.route('/403')
    def forbidden_error():
        abort(403)

    @testing_app.route('/500')
    def internal_server_error():
        abort(500)

    @testing_app.route('/general_exception')
    def general_server_error():
        raise Exception('A general exception')

    testing_client = testing_app.test_client()

    ctx = testing_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='function')
def test_client_csrf():
    """
    sets up a client to use in the tests
    :return:
    :rtype:
    """
    testing_app = create_app('testing')

    # set-up some error routes
    @testing_app.route('/403')
    def forbidden_error():
        abort(403)

    @testing_app.route('/500')
    def internal_server_error():
        abort(500)

    testing_app.test_client_class = FlaskClient
    testing_client = testing_app.test_client()

    ctx = testing_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='function')
def init_database():
    """
    sets up the database ready for the tests
    creates an initial test user
    :return:
    :rtype:
    """
    db.drop_all()
    db.create_all()
    user = User(username=TEST_USER_USERNAME, email=TEST_USER_EMAIL)
    user.set_password(TEST_USER_PASSWORD)
    db.session.add(user)
    db.session.commit()

    yield db

    db.session.close()
    db.drop_all()
