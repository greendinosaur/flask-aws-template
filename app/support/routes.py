from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from app.models import User
from app.services import utils
from app.support import bp
from app.support.forms import FeedbackForm


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
