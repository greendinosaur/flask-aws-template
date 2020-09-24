import os
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes

if os.getenv('FLASK_CONFIG') in ['development', 'testing']:
    # add in some simple forms to allow testing without using Auth0 for authentication
    # assumes there is already a test user inside the database that can be used
    bp.add_url_rule('/login', 'login', routes.login, methods=['GET', 'POST'])
    bp.add_url_rule('/logout', 'logout', routes.logout)
