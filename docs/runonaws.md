# Running the app on AWS

There are a few steps to perform in order to run the application on the AWS Elastic Beanstalk PaaS offering. These steps are detaield below.

## Set-up Elastic Beanstalk

You need to register an application on Elastic Beanstalk and create a Python environment.
To do this:
* Register for an AWS account if you haven't done so already
* If you're unfamiliar with Elastic Beanstalk, read the [documentation] (https://docs.aws.amazon.com/elastic-beanstalk/index.html)

### Install the EB CLI

The AWS CLI makes it easy to manage deployments and environment creation via the command line. Follow the [instructions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html) to install it via pip.

### Using the EB CLI to create and deploy a new application

Once installed, you need to configure your application and environment. 

Inside the flask-aws-template folder that contains the code, execute:

```commandline
eb init
```

Follow the prompts to fully set up the EB CLI and to define the application.
0. If you have not used AWS Command Line tools before, you will likely be asked for a username and password. For now, easiest to use the one used to register with AWS. 
1. Choose a suitable region where the application will be hosted
2. Choose an application name. The defualt is fine.
3. If it asks you about using Docker, say n
4. Choose Python as the platform
5. Choose Python 3.7 with Amazon Linux 2 as the runtime. This should be the default option.
6. Choose n to using code commit
7. Choose n to using SSH

You can now create your first environment: Enter

```commandline
eb init
```

Follow the prompts and answer as:
1. Say y to  the default environment name
2. Say y to the default prefix
3. Say y to the default load balancer (Application)
4. Say n to Spot Fleet

After answering these prompts, it will go about creating your environment. This will take a number of minutes.

As part of the initial environment creation, it will also deploy your code from your git repo. It will deploy the latest code on the master branch.

The final message on success will be something like `Successfully launched environment xxx` where xxx is the name of the environment.

Make a note of the security group listed on the line `Created security group named: xxxx` as you will require this security group in order to access the RDS database. See the later section for information on this.

To check all is okay, enter:

```commandline
eb health
```

This will show the health of the new environment. All being well, it will show a Status of Ready and a Health of Green.

Make a note of the `CNAME` of your application. This will be required if you set-up Auth0 as the authentication mechanism for your application.

Execute the following command to launch the URL for the environment in your default browser

```commandline
eb open
```

You should now see the default Flask app running successfully 😃 As the necessary environment variables to use Auth0 have not been set-up, you will not be able to login or register a new account just yet.

### Configure the application to use Auth0

Follow the guidance inside the [Introduction to Auth0](authentication.md) to create an Auth0 account. 

When you configure your application on the Auth0 website, make sure you add the CNAME of your Elastic Beanstalk environment to the callback URLs. You can do this in addition to the 127.0.0.1 as multiple callback domains are allowed.

### Deploying application changes to Elastic Beanstalk
You can deploy the application to Elastic Beanstalk using the EB CLI. By default, it deploys the latest version on the master branch.

Use the following to deploy changes. This will deploy to the environment created previously and restart it so the code changes take effect.

 ```commandline
eb deploy
```

## Set-up the database

Now you need to create a database. I recommend you do this separately and not as part of the Elastic Beanstalk environment. It's a more realistic scenario to have a separate database especially if you're running the application in Production. This [article](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html) has information on RDS databases and Elastic Beankstalk.

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

