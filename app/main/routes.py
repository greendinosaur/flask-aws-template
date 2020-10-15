from datetime import datetime

from flask import Blueprint
from flask import render_template, url_for, current_app, send_from_directory, request
from flask_login import current_user, login_required

from app.models import User
from app import db

bp = Blueprint('main', __name__)


@bp.before_request
def before_request():
    """
    Tracks the date/time the user last logged in and used the application
    :return:
    :rtype:
    """
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/welcome', methods=['GET'])
def welcome():
    """
    shows the welcome page
    :return:
    :rtype:
    """
    return render_template('welcome.html', title='Welcome')


@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    """
    shows the user's regular activities in order for them to log it
    :return:
    :rtype:
    """
    return render_template('index.html', title='Home',
                           form_url=url_for('main.index'))


@bp.route('/user')
@login_required
def user():
    """
    shows the user's profile
    :return:
    :rtype:
    """
    my_user = User.query.filter_by(id=current_user.get_id()).first_or_404()

    return render_template('auth/user.html', user=my_user)


@bp.route('/about', methods=['GET'])
def view_about():
    """
    shows the about page
    :return:
    :rtype:
    """
    return render_template('about.html', title="About Flask AWS Template")


@bp.route('/service-worker.js', methods=['GET'])
def service_worker():
    """
    returns the service-work js file that is required to make the app a full PWA one accessible on mobiles
    easiest to serve this at the root of the application, otherwise there are scope problems with the service worker
    and it cannot access other files
    Alternative is to serve it from the static folder but then the proxy (nginx) needs to send a http header
    :return:
    :rtype:
    """
    return current_app.send_static_file('service-worker.js')


@bp.route('/robots.txt')
@bp.route('/sitemap.xml')
def static_from_root():
    """
    serves the static files used by search crawlers
    these are referred to in the base URL but are served from the static folder
    :return:
    :rtype:
    """
    return send_from_directory(current_app.static_folder, request.path[1:])
