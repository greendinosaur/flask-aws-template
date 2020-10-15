from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

# create these variables here to avoid circular dependencies
# assumption is they will be imported in the main __init__.py file that is called to launch the application
# they will then be initialised in the create_app() function and available for use
db = SQLAlchemy()
oauth = OAuth()
