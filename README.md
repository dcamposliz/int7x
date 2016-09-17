# INT7x

INT7x is the **x** iteration of the Inertia7 Project, a platform for you to learn, build, and publish data science projects.

--

This README file contains documentation on technical requirements for running this app in development as well as in production, creating superuser accounts for admin purposes, as well as using the admin site.

--

## Requirements

This web app is built on Django 1.10. Check out the [Django Docs](https://docs.djangoproject.com/en/1.10/releases/1.10.1/).

--

### Install Django

Python 3 is a pre-requisite to Django. Once you install Python 3, run from the terminal:

    pip install django

--

## Deployment

Check the Wiki.

--

## Using the Administrative Settings

The admin site contains the forms to create new pages.

--

### Prerequisite: Create a superuser

From the command line, type:

    python manage.py createsuperuser

You will then be prompted to enter a username, email and password.

### Using the Admin Site
Go to http://(site this app is hosted on)/admin/ and sign in with your credentials.
