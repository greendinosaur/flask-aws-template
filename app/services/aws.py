import boto3
import botocore

from flask import current_app


def save_s3(bucket, name, contents):
    """
    Saves the contents to the file called name inside the provided bucket
    Assumes AWS credentials are available.
    Any errors are logged and function continues.

    :param bucket: bucket to save to
    :type bucket: string
    :param name: filename
    :type name: string
    :param contents: contents to write to file
    :type contents: string
    :return: Boolean indicating success or not. If an exception has occurred
    then False will be returned.
    :rtype: Boolean
    """
    try:
        s3 = boto3.resource('s3')
        s3.Object(bucket, name).put(Body=contents)
        return True

    except botocore.exceptions.ClientError as error:
        current_app.logger.error('Failed to save to s3: {}'.format(error))
        return False

    except botocore.exceptions.ParamValidationError as error:
        current_app.logger.error('Failed to save to s3: {}'.format(error))
        return False
