from flask import render_template

from app.support import bp


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
