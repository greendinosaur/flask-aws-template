# flask-aws-template
This application showcases a bare-bones Flask application that can be easily deployed to AWS Elastic Beanstalk.
The application is a fully responsive PWA website with some useful features that many applications require e.g. user authentication, logging etc.

# Motivation
I started to build a Flask based responsive website to run on AWS. I spent a lot of time searching for the best way to run a fully responsive PWA website built in Flask running on AWS. I could not find a complete working example to use as a starting point. I've decided to create this repo to showcase the way I did this so others can benefit from my learning.

# Status
The application is fully working.

Check it out by forking the repo and running locally


# Technology
It's built in Python leveraging the [Flask](https://flask.palletsprojects.com/en/1.1.x/#) framework. 
I've been using Python 3.7.7.

It requires a database backend. I've tested it under MySQL. Database access is performed via SQLAlchemy so theoretically other databases should work providing the relevant driver is installed.

The front-end uses the [Bootstrap](https://getbootstrap.com/) framework in order to provide a responsive UI. It works on mobile browsers as well as traditional Chrome, Safari and Brave on the desktop.
[FontAwesome](https://fontawesome.com) is also used to provide icons.

The [Auth0](https://auth0.com/) website is used for authentication. I use the Python Authlib package to assist with the authentication.
Strava APIs are used for integration with [Strava](https://www.strava.com).

Google Analytics tracking is provided in all of the HTML pages.

It is a fully PWA compliant application so can be readily installed on Android and iOS devices.

The requirements.txt file contains the dependent python packages that must be installed.

# Features

This app contains the following features:
* Use of Bootstrap and FontAwesome to produce a fully responsive, good-looking website
* A homepage and navbar built from Bootstrap
* Static pages required by many sites (FAQ, disclaimer, cookie policy, privacy policy)
* Contact Us page showcasing how to use AWS S3 to store the user submitted data
* Sign-up/Log-in/Log-out using Auth0 as the authentication provider
* A fully responsive PWA application that runs as well on the desktop as it does on a mobile device
* Database access via SQLAlchemy
* Google analytics
* Use of a Content Distribution Network (CDN) to serve the static content
* Pages contain the metadata required by search engines
* Metadata files required for PWA applications (manifest.json, service-worker.js, offline.html)
* Robust server-side error logging
* Showcases the use of CircleCI for a full CI/CD pipeline that runs automated tests and will deploy to AWS


# Installation

It's a standard Flask app with a database backend. To install and run locally:

## Run locally (non-Docker)

### Step 1 -  ensure Python is installed. 

It's been tested with Python 3.7.7.

### Step 2 - Fork this repo

Fork this repo, enter the following on the command line in the folder where you wish the code to live
```commandline
git clone <path to repo>
```

Now change into the directory
```commandline
cd flask-aws-template
```

### Step 3 - install the dependencies in a virtual environment

create the virtual environment
```commandline
python -m venv .venv
```

now activate the virtual environment
```commandline
source ./.venv/bin/activate
```

install the requirements
```commandline
pip install -r requirements.txt
```

### Step 4 - Set-up the initial environment variables

Some environment variables are required to launch the app

```commandline
export FLASK_APP=my_app
```

### Step 5 - Set-up the Flask logger
The logging configuration file [log_config.yaml](log_config.yaml) contains the configuration for the logger. 

It logs messages to a log file contained at `/tmp/my_app.log`. This may not be suitable for your environment so change the value in this file.

### Step 6 - set-up a database

A database is required. It will default to sqlite which is installed by default on many OS's.
Once you have a database, update the connection string. Otherwise, it will default to a local sqlite one which is fine for development.

```commandline
export DEV_DATABASE_URL=<YOUR DATABASE CONNECTION STRING>
```

### Step 7 - initialise the database

SQLAlchemy and Alembic are used to initialise the database

```commandline
flask db upgrade
```

### Step 8 - Launch the app

You can now run the app

```commandline
flask run
```

You should see a statement on the command line indicating the app is now ready at localhost:5000

Open up a browser to `http://localhost:5000`. Click around. Not all functionality will be working just yet as you need to register with some providers

### Step 9 - Set-up user authentication
The app uses [Auth0](https://auth0.com/) as its user authentication provider. You need to register for a free account with Auth0. Follow the guidance here to not only set-up your free account but also configure your tenant.

The import data you require once you have registered and have a tenant is the CLIENT_ID, CLIENT_SECRET, CLIENT_DOMAIN. Flask needs these set-up as environment variables. Execute the following

```commandline
export FLASK_CLIENT_ID=<YOUR_CLIENT_ID>
export FLASK_SECRET_ID=<YOUR_SECRET_ID>
export FLASK_CLIENT_DOMAIN=<YOUR_DOMAIN>
```
If you restart the application with `flask run`, the sign-up, log-in and log-out links will now work.

### Step 10 - (Optional) Set-up Google analytics

If you have a web-domain and wish to use [Google Analytics](https://analytics.google.com/) for this Flask apo, then you will need to register with google. Follow their guidance here.

Once you've done this, set-up the relevant environment variable

```commandline
export GA_CODE=<YOUR_GOOGLE_TAG>
```

### Step 11 - (Optional) Set-up an AWS S3 bucket to store feedback from the Contact Us page

To fully use the contact-us page, you will need an AWS S3 bucket. Once you have one

```commandline
export S3_BUCKET
```

### Step 12 - (Optional) Set-up a CDN to servce static content

If you'd like to use a CDN to serve the static content then register and set-this up. Once you have the URL for the CDN then you need to let Flask know.

```commandline
export CDN_DOMAIN-<YOUR_CDN_DOMAIN>
```

## Run via Docker
Or you can use the [Dockerfile](Dockerfile) and [docker-compose file](docker-compose.yml) to launch the Flask app in a container connected to MySQl running in a container. 

Make sure Docker is running locally and then enter:

```commandline
docker-compose build
```

followed by

```commandline
docker-compose up
```

Follow the instructions in the previous section for setting up Auth0, Google Analytics, AWs S3 bucket and your CDN.

## Running in the cloud

This application will readily run in AWS. I've used:
* Elastic Beanstalk to run the Flask application
* The Flask applications connects to RMS with a MySQL database
* S3 to store the Contact Us queries as json files
* Route 53 to route requests to a load-balancer in front of Elastic Beanstalk 
* Cloudfront as a CDN to serve the application's static files (images, css, js) from a dedicated S3 Bucket

CircleCI is used to automatically deploy the application to Elastic Beanstalk and the static files to S3.

TODO - Instructions on setting up AWS

## Tests and CI/CD

### Tests
The tests folder contains all of the application tests.
Selenium is used in headless mode to test the UI. [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) will need to be installed.

To run the tests execute `Make test` on the command line.
You can also run various linters by entering `Make lint`. These will provide some errors due to the way Flask works.

### CI/CD

I've leveraged [CircleCI](https://circleci.com) for Continuous Integration and Continuous Deployment. Tests are automatically run the against a MySQL database. Builds on master are automatically deployed when all tests pass successfully. Check out the [config file](.circleci/config.yml)

I've also used [SonarCloud](https://sonarcloud.io) to highlight code coverage and code quality issues.

[Snyk](https://snyk.io) is used to scan the requirements.txt file for potential vulnerabilities.

## How to use?
Take this code as is and alter to better suit your needs.
* You can add new imagery and styles. Alter the files in the [static](app/static) folder
* Change the [templates](app/templates)
* Change the [code](app) 
* update the meta data in the [base template](app/templates/base.html) to better support your site

## Contribute
Feedback and contributions are welcome. 

## To dos
* Update this documentation to run the app in AWS

# License
This is licensed under a MIT licence.

