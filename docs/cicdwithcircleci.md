# Overview

[CircleCI](https://circleci.com) has been used to provide CI/CD for this Flask application. This document describes the use of CircleCI in detail and how to configure it for your forked repo.

## CircleCI pipeline

The file [config.yml](../.circleci/config.yml) contains the configuration of the CircleCI pipeline.

There are two main jobs.

### build-and-test

This runs whenever code is committed to a branch or master in the Github repo.

It essentially builds the application, runs it in a Docker container and runs the application tests.
It runs the tests against a MySQL database.
The test files are stored as part of the build so they can be retrieved later.

### deploy

This runs when a change is made to Master. It runs following completion of the build-and-test job.

This job will deploy the application to AWS. It deploys all static content (images, javascript etc.) to an S3 bucket and the actual Flask application to an Elastic Beanstalk environment.

There is a manual step required which requires a user to click Approve within the Hold step which authorizes the deployment to go ahead

To configure this job, you will need to define some environment variables inside CircleCI. This is done inside a context called `AWS` within your CircleCI Organization.

Specifically:
* `BEANSTALK_APPLICATION_NAME` is the name of your Elastic Beanstalk application
* `BEANSTALK_ENVIRONMENT_NAME` is the name of your environment to deploy to
* `AWS_S3_BUCKET` is the name of the S3 bucket used to host static content.
* `AWS_ACCESS_KEY_ID` is the name of the AWS key that has permission to deploy to AWS
* `AWS_SECRET_ACCESS_KEY_ID` is the associated secret for the AWS Key
* `AWS_DEFAULT_REGION` is the default region that AWS will use
* `AWS_REGION` is the region hosting the application. 

## CircleCI setup

In order to use these pipelines, you will need to:
* ensure you have an account with CircleCI. This is free.
* add details of your Github account to CircleCI
* setup a project within CircleCI that connects to your repo containing this Flask app
* when setting up the project in CircleCI, tell it you already have a .circleci configuration file to use and do not use the default one that it proposes
* If you'd like to automatically deploy your application to AWS then you will need to set-up the above mentioned environment variables.

CircleCI will build any changes committed to any branch or master.




