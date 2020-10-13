# flask-aws-template
This application showcases a fully responsive PWA website with some useful features that many applications require e.g. user authentication, logging, privacy statements, SEO ready etc.

It's built entirely in Python and Flask. It runs easily on AWS: guidance on installing on AWS Elastic Beanstalk is provided.

It will also run on other cloud providers.

It's been designed as a template so you can take a copy of this repo and customize to your requirements.

# Motivation
I started to build a Flask based responsive website. I spent a lot of time searching for the best way to run a fully responsive PWA website built in Flask running on AWS. I could not find a complete working example to use as a starting point. I've decided to create this repo to showcase the way I did this so others can benefit from my learning.

I also spent a lot of time building some of the "compliance/hygiene" type pages like Contact Us, Privacy Policy etc. that every website requires. I thought it would be useful to have a working Flask application that has these plumbed in and ready for customization. This means less time on those type of features and more on the value-add product differentiators you really want to be working on.

Another motivation is I believe in using SaaS services and not re-inventing the wheel especially when it comes to super-sensitive topics like User Authentication and Sign-Up. There is no need to be building yet-another-authentication piece of code when you can trust companies like Auth0 to do this. Far better to plug into SaaS offerings like Auth0 that provide commodity services so you can once again focus on the value-adds.

Furthermore, it's not only features that you need to care about. It's also SEO, tracking product analytics etc. This is why I've also added the use of Google Analytics tracking and various tags/best practice to assist with SEO so people actually find your site.

And finally...... good engineering practices are a must. CI/CD and code quality are critical. Why spend ages trying to construct a pipeline that builds, tests and deploys the application when you can re-use an existing one. Learn how to use tools such as CircleCI, SonarCloud and Snyk to help improve your application. This sample app shows some of these tools in use.

# Status
The application is fully working.

Check it out by generating a copy of the repo and run it locally.

Note that whilst this app runs on AWS, this application will work on other cloud platforms of your choice. It has [Docker](Dockerfile) and [docker-compose](docker-compose.yml) files available that can be utilised to run on other platforms.

# Technology
It's built in Python leveraging the [Flask](https://flask.palletsprojects.com/en/1.1.x/#) framework. 
I've been using Python 3.7.7.

It requires a database backend. I've tested it under MySQL. Database access is performed via SQLAlchemy so theoretically other databases should work providing the relevant driver is installed.

The front-end uses the [Bootstrap](https://getbootstrap.com/) framework in order to provide a responsive UI. It works on mobile browsers as well as traditional Chrome, Safari and Brave on the desktop.
[FontAwesome](https://fontawesome.com) is also used to provide icons.

The [Auth0](https://auth0.com/) website is used for authentication. I use the Python Authlib package to assist with the authentication.

[Google Analytics tracking](https://marketingplatform.google.com/about/analytics/) is supported in all of the HTML pages.

It is a fully [PWA compliant](https://web.dev/progressive-web-apps/) application so can be readily installed on Android and iOS devices. [Lighthouse](https://developers.google.com/web/tools/lighthouse/) in the Chrome DevTools has been used to test the compliance of the application.

The [requirements.txt](requirements.txt) file contains the dependent python packages to be installed.

# Features

This app contains the following features:
* Use of Bootstrap and FontAwesome to produce a fully responsive, good-looking website.
* A homepage and navbar built from Bootstrap
* Static pages required by many sites (FAQ, disclaimer, cookie policy, privacy policy)
* Displays a use of cookies banner that must be clicked to acknowledge the use of cookies
* Contact Us page showcasing how to use AWS S3 to store the user submitted data
* Sign-up/Log-in/Log-out using Auth0 as the authentication provider
* A fully responsive PWA application that runs as well on the desktop as it does on a mobile device
* Database access via SQLAlchemy so agnostic to underlying database used
* Incorporates Google analytics tracking
* Use of a Content Distribution Network (CDN) to serve the static content
* Pages contain the metadata required by search engines
* Metadata files required for PWA applications (manifest.json, service-worker.js, offline.html)
* Robust server-side error logging
* Showcases the use of CircleCI for a full CI/CD pipeline that runs automated tests and will deploy to AWS


# Installation

It's a standard Flask app with a database backend. To install and run locally:

## Run locally (non-Docker)

### Step 1 -  ensure Python and Pip are installed. 

It's been tested with Python 3.7.7. It should work with any versions of Python >= 3.7.

### Step 2 - Create your repo

This repo has been marked as a template. This means you can easily create your own copy as a starting point.

Click [generate](https://github.com/greendinosaur/flask-aws-template/generate) to generate your own copy of this repo.

Once you've generated your own copy of the repo, you will need to clone this repo onto your local machine.

Inside the directory where you wish to store the code enter:

```commandline
git clone=<yourrepo>
```

### Step 3 - install the dependencies in a virtual environment

Change directories into the directory containing your copy of the source code.

You need to create a virtual environment inside this directory.

```commandline
python -m venv .venv
```

now activate this virtual environment
```commandline
source ./.venv/bin/activate
```

install the requirements into this virtual environment
```commandline
pip install -r requirements.txt
```

### Step 4 - Set-up the initial environment variables

Two initial environment variables are required to launch the app

```commandline
export FLASK_APP=my_app
export FLASK_CONFIG=development
```

### Step 5 - Set-up the Flask logger
The logging configuration file [log_config.yaml](log_config.yaml) contains the default configuration for the logger. 

It logs messages to a log file called `my_app.log` at `/tmp/my_app.log`. This may not be suitable for your environment so change the value in this file.

### Step 6 - set-up a database

A database is required. It will default to sqlite which is installed by default on many OS's.

If you have a database, update the environment variable that stores the connection string. Otherwise, it will default to a local sqlite one which is fine for development.

```commandline
export DEV_DATABASE_URL=<YOUR DATABASE CONNECTION STRING>
```

### Step 7 - initialise the database

If you have a database, use SQLALchemy and Alembic to set-up this database with the required tables.

```commandline
flask db upgrade
```

### Step 8 - Launch the app

You can now run the app

```commandline
flask run
```

You should see a statement on the command line indicating the app is now ready at localhost:5000

Open up a browser to [http://localhost:5000](http://localhost:5000). Click around. Not all functionality will be working just yet as you need to register with some providers

### Step 9 - (Optional) Set-up user authentication
The app uses [Auth0](https://auth0.com/) as its user authentication provider. You need to register for a free account with Auth0. Follow the guidance here to not only set-up your free account but also configure your tenant.

The wiki article [Authentication](https://github.com/greendinosaur/flask-aws-template/wiki/Authentication) describes the Auth0 setup in further details along with an explanation of how the app has been coded to use Auth0.

The important data required, once you have registered and have a tenant, is the *CLIENT_ID*, *SECRET*, *DOMAIN*. Flask needs these set-up as environment variables. Execute the following

```commandline
export AUTH0_CLIENT_ID=<YOUR_CLIENT_ID>
export AUTH0_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
export AUTH0_CLIENT_DOMAIN=<YOUR_DOMAIN>
```
If you restart the application with `flask run`, the sign-up, log-in and log-out links will now work.

### Step 10 - (Optional) Set-up Google analytics

If you have a web-domain and wish to use [Google Analytics](https://analytics.google.com/) for this Flask app, then you will need to register with Google. Follow the guidance on the [Google Analytics](https://analytics.google.com/) site.

Once you've done this, set-up the relevant environment variable

```commandline
export GA_CODE=<YOUR_GOOGLE_TAG>
```

### Step 11 - (Optional) Set-up an AWS S3 bucket to store feedback from the Contact Us page

To fully use the contact-us page, you will need an AWS S3 bucket. Once you have one set-up, the following environment variables:

```commandline
export CONTACT_US_FORMAT=S3
export S3_BUCKET=<NAME_OF_BUCKET
```

### Step 12 - (Optional) Set-up a CDN to serve static content

If you'd like to use a CDN to serve the static content then register and set-this up. Once you have the URL for the CDN then you need to let Flask know.

```commandline
export CDN_DOMAIN=<YOUR_CDN_DOMAIN>
```

You will need to ensure all of the content (files and subfolders) inside the `static` folder is deployed to your CDN so it is accessible as `https://<YOUR_CDN_DOMAIN/static/...`

### Finally
If you've followed the previous steps then you will have a fully running Flask instance demonstrating some essential features. 
* The Flask app will be using Auth0 to manage user authentication and sign-ups. 
* It will serve the static content from the CDN so end users get better page load times.
* Google Analytics will be tracking usage of your site so you can start to see visitor numbers, pages accessed etc.
* You're all set for customer engagement via the Contact Us page.
* It is a PWA so can easily be used and installed on mobile devices without requiring the relevant app store 
* Basic, compliance type features are readily available which you can customize for your own use.

## Run via Docker

You can use the [Dockerfile](Dockerfile) and [docker-compose file](docker-compose.yml) to launch the Flask app in a container connected to MySQl running in a container. 

Make sure Docker is installed and running locally and then enter:

```commandline
docker-compose build
```

followed by

```commandline
docker-compose up
```

Follow the instructions in the previous section for setting up Auth0, Google Analytics, AWS S3 bucket and your CDN. 

The environment variables will need to be set-up locally within your shell as the docker-compose command passes the local environment variables to the container. See [docker-compose](docker-compose.yml).

## Running in the cloud

This application will readily run in AWS and, as a bonus, on the free tier. I've used:
* Elastic Beanstalk to run the Flask application
* The Flask applications connects to RMS with a MySQL database
* S3 to store the Contact Us queries as json files
* Route 53 to route requests to a load-balancer in front of Elastic Beanstalk 
* Cloudfront as a CDN to serve the application's static files (images, css, js) from a dedicated S3 Bucket

CircleCI is used to automatically deploy the application to Elastic Beanstalk and the static files to S3.

[Running on AWS](https://github.com/greendinosaur/flask-aws-template/wiki/Running-the-Flask-app-on-AWS) describes the AWS set-up required to run the Flask app on the AWS Elastic Beanstalk PaaS.

It can be deployed to other cloud providers as it is a simple Flask app. 

## Tests and CI/CD

### Tests
The [tests](app/tests) folder contains all of the application tests. These use the pytest framework. They test the database, views, business logic and the UI.

Selenium is used in headless mode to test the UI. [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) will need to be installed.

Prior to running the tests, you will need to ensure the `TEST_DATABASE_URL` environment variable is set. You could either test against a simple sqllite database in which case set the variable as follows

```commandline
export TEST_DATABASE_URL=sqlite:///test_app.db
```

or if you have a MySQL or other database available then enter

```commandline
export TEST_DATABASE_URL=<connection string>
```

or if you run `docker-compose up --build` to run the app then you can connect to the mysql database server running in the container as

```commandline
export TEST_DATABASE_URL=mysql+pymysql://root:hello@localhost:3308/test?charset=utf8mb4
```

To run the tests execute `Make test` on the command line. 

The [Lighthouse](https://developers.google.com/web/tools/lighthouse/) component of Google Chrome Dev Tools has been heavily used to ensure the application is SEO ready and fully PWA compliant.

### CI/CD

I've leveraged [CircleCI](https://circleci.com) for Continuous Integration and Continuous Deployment. Tests are automatically run the against a MySQL database. Builds on master are automatically deployed when all tests pass successfully. 

Check out the [config file](.circleci/config.yml) and the [CircleCI overview](https://github.com/greendinosaur/flask-aws-template/wiki/Running-the-Flask-app-on-AWS) for further details on using CircleCI.

## Further information

Take a look at the project [wiki](https://github.com/greendinosaur/flask-aws-template/wiki) for further guidance on using this template as a starting point for your own Flask based applications.

## How to customize?

Take this code as is and alter to better suit your needs.
* You can add new imagery and styles. Alter the files in the [static](app/static) folder
* Change the [templates](app/templates)
* Change the [code](app) 
* Update the meta data in the [base template](app/templates/base.html) to better support your site

## Contribute
Feedback and contributions are welcome. Checkout the [code of conduct](CODE_OF_CONDUCT.md) and [contributor guidelines](CONTRIBUTING.md).

## To dos
* The [issue tracker](issues) contains the proposed enhancements and bug fixes.

# License
This is licensed under a MIT licence.

