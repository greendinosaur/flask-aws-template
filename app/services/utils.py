import json
import os
import uuid
from datetime import datetime

import pytz

from app.services import aws


def localize_local_time(user_datetime: datetime, user_tz='UTC'):
    """
    localises the provided time into the provided timezone
    :param user_datetime:datetime to localise
    :type user_datetime: datetime
    :param user_tz: timezone to localize into
    :type user_tz: tiemzone
    :return: the localized datetime
    :rtype: datetime
    """
    local_tz = pytz.timezone('UTC')
    try:
        # check the timezone provided is valid
        local_tz = pytz.timezone(user_tz)
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    local_dt = local_tz.localize(user_datetime)
    return local_dt


def get_utc_from_local_time(user_datetime: datetime, user_tz='UTC'):
    """
    Converts a datetime from the user's TZ into UTC datetime
    :param user_datetime: the datetime in the user's TZ
    :type user_datetime: datetime
    :param user_tz: the user's Timezone
    :type user_tz: Timezone
    :return: a datetime in UTC
    :rtype: Datetime
    """
    local_tz = pytz.timezone('UTC')
    try:
        # check the timezone provided is valid
        local_tz = pytz.timezone(user_tz)
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    local_dt = local_tz.localize(user_datetime)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt


def get_local_time_from_utc(user_datetime: datetime, user_tz='UTC'):
    """
    Converts a datetime from UTC into the user's timezone
    :param user_datetime: the datetime in the user's TZ
    :type user_datetime: datetime
    :param user_tz: the user's Timezone
    :type user_tz: Timezone
    :return: a datetime in user's local time
    :rtype: Datetime
    """
    local_tz = pytz.timezone('UTC')
    try:
        # check the timezone provided is valid
        local_tz = pytz.timezone(user_tz)
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    utc_tz = pytz.timezone('UTC')
    utc_date = utc_tz.localize(user_datetime)
    local_dt = utc_date.astimezone(local_tz)

    return local_dt


def get_iso_from_local_time(user_datetime: datetime):
    """
    outputs the provided datetime into an ISO date format string
    :param user_datetime: the datetime in the user's TZ
    :type user_datetime: datetime
    :return: provided datetime formatted into a ISO string
    :rtype: string
    """
    return user_datetime.isoformat()


def generate_random_filename_from_email(email):
    """
    returns a filename with some random characters infront of part of the email
    the part of the email prior to the @ is used to generate the filename
    :param email: email address
    :type email:
    :return: the filename
    :rtype:
    """
    email_prefix = email[:email.index("@")]
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), email_prefix, '.json'])

    return random_file_name


def save_contents_file(email, contents):
    """
    Saves the received feedback to a file.
    This will be on S3 or the local filesystem dependent on the environment property
    CONTACT_US_FORMAT=S3, saves to S3 otherwise saves to file system
    The env variable S3_BUCKET indicates the S3 bucket to use

    :param email: email address of person providing feedback
    :type email: string
    :param contents: contents of the feedback
    :type contents: json
    :return: whether the save was a success or not
    :rtype: Boolean
    """
    filename = generate_random_filename_from_email(email)

    # check to see if to save to AWS or filesystem
    if os.getenv('CONTACT_US_FORMAT') == 'S3':
        return aws.save_s3(os.getenv('S3_BUCKET'), filename, json.dumps(contents))

    # write to file otherwise
    with open(filename, 'w') as outfile:
        json.dump(contents, outfile)
        return True


def get_os_env(default, key):
    """

    :param default: the default value if the key does not exist
    :type default: str
    :param key: the environment variable to look for
    :type key: str
    :return: the value of the environment variable if it exists, otherwise the provided default value
    :rtype:
    """
    return os.getenv(key, default)
