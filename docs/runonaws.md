# Running the app on AWS

There are a few steps to perform in order to run the application on the AWS Elastic Beanstalk PaaS offering. These steps are detaield below.

## Set-up Elastic Beanstalk

You need to register an application on Elastic Beanstalk and create a Python environment.
To do this:
* Register for an AWS account if you haven't done so already
* If you're unfamiliar with Elastic Beanstalk, read the [documentation] (https://docs.aws.amazon.com/elastic-beanstalk/index.html)

### Create an Application

An application must be created. Follow the [AWS instructions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications.html) to create a new application.

Once an application is created, you will be guided to create an environment to host and run the application.

### Create an Environment

The [AWS Documents](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.environments.html) cover the creation of a new environment via the AWS Management console.

Remember to select a Web Server Environment and in the Platform options, Managed platform, Python as the Platform and Python 3.7 running on 64bit Amazon Linux 2 as the branch. Leave the Platform version as the Recommended version. You can leave other options at the defaults.

To get going, it's best to deploy the sample application provided by AWS so you can check the application and environment is working. 


### Test the environment

Once the environment is created, you will see the name of the environment and its URL. Click on the URL and you will see the default application installed by AWS.

## Set-up the database

Now you need to create a database. I recommend you do this separately and not as part of the Elastic Beankstalk environment. It's a more realistic scenario to have a separate database especially if you're running the application in Production. This [article](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html) has information on RDS databases and Elastic Beankstalk.

To create the database, go to the RDS services. You can then create a database.

This application has been tested with a MySQL database v5.7.x.

When setting up the database:
1. Choose Standard Create
2. Choose MySQL 5.7.31
3. In Templates, Choose the Free Tier so it won't cost you anything
4. Set DB Instance Identifier to my-flask-db
5. In credentials, set the master username to Flask and set the password to something you will remember
6. In additional connectivity configuration, set Public Access to Yes. This will enable you to connect to the database from your local machine.
7. In additional configuration, set the Initial database name to flask-example
8. You can leave all options at their default values.

Once the database is created, you need to configure security groups so Elastic Beanstalk can access the database as well as your local machine.

### Set-up database security groups

Follow the guidance on this [AWS page](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/rds-external-defaultvpc.html) to modify the inbound rules on your RDS instance's security group.

You should also add the IP address of your local machine to this security group and enable All traffic. This will allow you to connect to the database directly. This is useful to query the database and to run database migrations via the Flask-Migrate utility.

## Install the EB CLI

The AWS CLI makes it easy to manage deployments and environment creation via the command line. Follow the [instructions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html) to install it via pip.

## Configure EB CLI for Elastic Beanstalk

Once installed, you need to configure it before you can use it. Inside the flask-aws-template folder, execute:

```commandline
eb init
```

Follow the prompts to fully set up the EB CLI. 
* Choose the same region where you created the application and environment
* select the application and environment when prompted

Once you've set it up, check it's working by executing the following command to list all the environments for the application

```commandline
eb list
```

You can also execute the following command to launch the URL for the environment in your default browser

```commandline
eb open
```

## Deploying the application to Elastic Beanstalk
You can now deploy the application to Elastic Beanstalk using the EB CLI.

 ```commandline
eb deploy
```
