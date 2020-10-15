from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from app.models import User
from app.services import utils
from app.support.forms import FeedbackForm

bp = Blueprint('support', __name__)


@bp.route('/privacy', methods=['GET'])
def privacy():
    """
    shows the privacy page
    :return:
    :rtype:
    """
    return render_template('support/privacypolicy.html', title='Privacy Policy')


@bp.route('/disclaimer', methods=['GET'])
def disclaimer():
    """
    shows the disclaimer page
    :return:
    :rtype:
    """
    return render_template('support/disclaimer.html', title='Disclaimer')


@bp.route('/cookies', methods=['GET'])
def cookies():
    """
    shows the cookie page
    :return:
    :rtype:
    """
    return render_template('support/cookies.html', title='Cookies')


@bp.route('/faq', methods=['GET'])
def faq():
    """
    shows the FAQ page
    :return:
    :rtype:
    """
    return render_template('support/faq.html', title='FAQ')


@bp.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = FeedbackForm()

    if form.validate_on_submit():
        # save the feedback
        utils.save_contents_file(form.email.data, form.to_json())
        flash('Thank you for sending us a note')
        return redirect(url_for('support.contact_us'))

    if current_user.is_authenticated:
        # can set the name and email on the form
        u = User.query.filter_by(id=current_user.get_id()).first()
        form.email.data = u.email
        form.name.data = u.username

    return render_template('support/contact_us.html', title='Contact Us', form=form)
