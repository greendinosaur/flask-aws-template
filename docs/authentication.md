# Authentication Overview

This Flask template uses a SaaS offering [Auth0](https://auth0.com) to provide user authentication capabilities including log-in, log-out and sign-up for new users. This includes the ability for a user to sign in using their social identity providers such as Google, Facebook or Twitter.

There are a number of reasons it uses an external service such as Auth0 for authenticaiton. These are:
* **Security**. An external service such as Auth0 has been designed from the ground-up to be secure. They take care of all the authentication logic, storage of sensitve data such as passwords and securiing all of this against intrusion. Building a secure application is difficult and it's advisable to leave it to the experts
* **Robust and scalable**. Such a service will scale as your userbase scales and can easily cope with large number of log-ins.
* **Feature rich**. It would take a long time to build a similar service from scratch with the same level of features. Better to leverage an existing one that is continually being extended. These enhancements benefit you and your users.
* **More time soent on value-adds**. By leveraging a SaaS service, you can spend more time building the value-adds and less on "commodity" type services such as user authentication

## Why Auth0

This templated app uses Auth0 as they have a generous free-tier which means you can use it for free and benefit from many of the features including authenticaiton, up-to two different social identity providers, email notifications to welcome new users etc.

There are many other authentication providers out there including [Amazon Cognito](https://aws.amazon.com/cognito/) that you may also want to explore. Pricing and features vary across the different providers.

## How to use Auth0 with this application

### Register for a free account with Auth0

You need to register a free account with Auth0. This will give you a tenant unique to you. From the tenant, you will need to create a Web Application. 

This Web Application is what users will interact with when they authenticate to your site via Auth0. You can configure this web application in a number of ways such as:
* the look-and-feel of the log-in and registration pages
* define the social providers you would like to offer to your users to log in as an alternative to a new username and password, 
* email templates to be used when sending welcome emails and other features. 
* etc.

The Auth0 website has extensive documentation and walks you through the set-up.

#### Minimum Auth0 Configuration required

Ensure you have the the values for the:
* *Client ID*
* *Client Secret* 
* *Domain* for your web application. 

These are shown on the Auth0 Applications page under Basic Information. With these, you can configure this templated app.

You also need to configure the callback URLs on the configuration page so Auth0 knows where to call back when it successfully authenticates a user to your application.

These callback URLS are set on the Application URIs part of the Basic Information page. Set them as:
* *Allowed Callback URL* to http://127.0.0.1:5000/callback
* *Allowed Logout URLS* to http://127.0.0.1:5000/welcome
* *Allowed Web Origins* to http://localhost:5000

You can leave other values at their default.

If you're interested in setting up Social Identity providers then checkout the *Connections* option on the left hand navbar. This guides you towards setting up Social providers. This will entail registering your application with each of the social providers and providing some configuraiton information with them and then further configuration information on Auth0. 

### Configure the Flask application

The Auth0 secrets need to be defined as environment variables as follows:

```commandline
export AUTH0_CLIENT_ID=<YOUR_CLIENT_ID>
export AUTH0_SECRET_ID=<YOUR_SECRET_ID>
export AUTH0_CLIENT_DOMAIN=<YOUR_DOMAIN>
```

### Test it out

Now restart your Flask application, either directly using Flask run or via docker-compose.

The application will be available at http://127.0.0.1

Click on the Sign-Up button. If it's all been configured correctly, then you should see the Auth0 sign-up screen. Register for an account and you will be taken to the home page of the Flask application.

## How does the Flask app work

 Under the hood, the Flask application uses something called OAuth to communicate with Auth0 and authenticate the user.
 
 A Python library called AuthLib does the heavy lifting so it's case of configuring it and then using it.
 
 The relevant pieces of code are in the following files.
 
 **[__init__.py](../app/__init__.py)**
 In here, you can see the import of the OAuth package from Authlib.
 
 You will also see the registration of Auth0 with the application. This utilises the environment variables defining the secrets for your Auth0 application.
 
 **[routes.py](../app/auth/routes.py)**
 This contains the code that calls Auth0 for login, logout and sign-up.
 
 There is a view called `login_new` that redirects the user to Auth0 for login.
 
 The `logout_new` view redirects the user to Auth0 for logout
 
 The `sign-up` view redirects the user to Auth0 for signing up. This is to register new users as the Auth0 Sign-up form is a little different to the login form.
 
 The `authorize` view redirects the user to Auth0 for login.
 
 Both the `authorize` and `sign-up` view set-up Auth0 to callback the callback view when it has successfully authenticated the user.
 
 Inside the `callback` view, the function retrieves some key data about the user (name, email address, profile image) and persists this to the database. It checks to see if this is a new user and will create a new user record where necessary,
 
 The `callback` view, also utilises the Flask-Login module to log the user into the Flask module. This Flask-Login module helps control access to the views depending on whether the user is logged in or not.
 
 ### Note on Testing
 
 To avoid accessing Auth0 when testing the app locally, there are simple `login` and `logout` views. You'll see that these aren't added to the list of views automatically via the `@bp.route` decorator. The reason for this is to not expose these views in a staging or production environment when we want users to login via Auth0. 
 
 Inside the packages [__init__.py](../app/auth/__init__.py) file is a piece of code that only adds these to the list of Flask routes if the `FLASK_ENV` variable is configured to `development` or `testing`.
 
 
