import os
from app import create_app

print(os.getenv('FLASK_CONFIG'))
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
