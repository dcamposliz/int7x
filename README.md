# INT7x

INT7x is the **x**'th iteration of the Inertia7 Project, a platform for you to learn, build, and publish data science projects.


This README file contains documentation on technical requirements for running this app in development as well as in production, creating superuser accounts for admin purposes, as well as using the admin site.

This web app is built on Django 1.10. Check out the [Django Docs](https://docs.djangoproject.com/en/1.10/releases/1.10.1/).

## DEVELOPMENT ENVIRONMENT SETUP

### Pre-requisites

**Python 3** and **Django 1.10** are required.

### Launching local server

You will need to include **db.sqlite3** and **INT7_DO_NOT_UPLOAD.py** within your project directory in order for the application to run. You can contact us if you would like a copy of these files.

Once you have all your dependencies met, type into the terminal:

	python manage.py runserver


## DEPLOYMENT TO PRODUCTION

### Pre-requisites

**Python 3** and **Django 1.10** are required.

At this point you should have:

 - An AWS EC2 instance running Ubuntu

 - SSH access to your EC2 instance

 - Python 3 installed your EC2 instance

 - The contents of this repository copied onto your EC2 instance and in a folder with name <project-folder-name>, where you substitute **project-folder-name** to a name of your choosing.

**Folder Structure:**

 - home

  - ubuntu

   - `<project-folder-name>`

    - inertia7

    - projects

    - static

    - templates

    - **db.sqlite3**

    - **INT7_DO_NOT_UPLOAD.py**

**db.sqlite3** and ** INT7_DO_NOT_UPLOAD.py ** are not located on the GitHub repository for security reasons but must be included within **<project-folder-name>** for the app to work.

### Instructions

This guide was adapted from Digital Ocean's tutorial [How To Serve Django Applications with Apache and mod_wsgi on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04).

#### Install the necessary software

	sudo apt-get update

	sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

#### Configure a Python Virtual Environment

**You should be in directory**: <project-folder-name>
	
This allows us to keep the tools (Python modules) our project needs separate from our base Python installation.
 
##### Install virtualenv

Type into the terminal:

	sudo pip3 install virtualenv
 
##### Create a Python virtual environment

Type into the terminal:

	virtualenv <virtual-env-name>


	








#############################

## ADMIN SETTINGS

The admin site contains the forms to create new users, projects, etcetera.


### Prerequisite: Create a superuser

From the command line, type:

    python manage.py createsuperuser

You will then be prompted to enter a username, email and password.


### Using the Admin Site
Go to http://(site this app is hosted on)/admin/ and sign in with your credentials.
