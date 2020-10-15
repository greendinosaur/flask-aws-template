import logging
from logging import config

import yaml

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cdn import CDN
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect

from app.services import utils
from app.db import db, oauth

from config import app_config

migrate = Migrate()
login = LoginManager()
login.login_view = 'main.welcome'
bootstrap = Bootstrap()
moment = Moment()
csrf = CSRFProtect()

cdn = CDN()


def create_app(config_name='default'):
    """
    Starts up the Flask application based on the supplied configuration
    :param config_class: Configuration to start the app with
    :type config_class:
    :return: the Flask app
    :rtype:
    """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)

    with open("log_config.yaml", 'rt') as f:
        config_data = yaml.safe_load(f.read())
        config.dictConfig(config_data)

    app.logger = logging.getLogger(app.config['LOGGING_CONFIG'])
    app.logger.error('starting the app')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
    cdn.init_app(app)

    oauth.init_app(app)
    oauth.register(
        'auth0',
        client_id=app.config['AUTH0_CLIENT_ID'],
        client_secret=app.config['AUTH0_CLIENT_SECRET'],
        api_base_url=app.config['AUTH0_CLIENT_DOMAIN'],
        access_token_url=app.config['AUTH0_CLIENT_DOMAIN'] + '/oauth/token',
        authorize_url=app.config['AUTH0_CLIENT_DOMAIN'] + '/authorize',
        client_kwargs={
            'scope': 'openid profile email',
        },
    )

    from app.errors.handlers import bp as errors_bp
    from app.auth.routes import bp as auth_bp
    from app.main.routes import bp as main_bp
    from app.support.legal_routes import bp as support_bp
    app.register_blueprint(errors_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(support_bp, url_prefix='/support')

    # this filter allows environment variables to be read inside the jinja templates
    app.jinja_env.filters['get_os_env'] = utils.get_os_env

    from app.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
