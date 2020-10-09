import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Flask specifics
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'you-will-never-guess'
    WTF_CSRF_SECRET_KEY = os.environ.get('CSRF_SECRET_KEY') or SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # details provided by Auth0 following registration of an app
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID') or ''
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET') or ''
    AUTH0_CLIENT_DOMAIN = os.environ.get('AUTH0_CLIENT_DOMAIN') or ''

    LOGGING_CONFIG = "development"

    CDN_DEBUG = False
    CDN_DOMAIN = os.environ.get('CDN_DOMAIN') or ''
    CDN_HTTPS = True
    CDN_TIMESTAMP = False

    # staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    CDN_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    LOGGING_CONFIG = "development"


class TestingConfig(Config):
    TESTING = True
    CDN_DEBUG = True
    LIVESERVER_PORT = 8943
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test_app.db')
    LOGGING_CONFIG = "test"


class StagingConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    CDN_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('STAGING_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'stage_app.db')
    LOGGING_CONFIG = "test"


class ProductionConfig(Config):
    DEBUG = False
    CDN_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'prod_app.db')
    LOGGING_CONFIG = "production"


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'default': DevelopmentConfig
}
