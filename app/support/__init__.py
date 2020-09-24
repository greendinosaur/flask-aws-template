from flask import Blueprint


bp = Blueprint('support', __name__)

from app.support import routes, legal_routes

