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

   - **`<project-folder-name>`**

    - inertia7

    - projects

    - static

    - templates

    - **db.sqlite3**

    - **INT7_DO_NOT_UPLOAD.py**

**db.sqlite3** and **INT7_DO_NOT_UPLOAD.py** are not located on the GitHub repository for security reasons but must be included within **`<project-folder-name>`** for the app to work.

### Instructions

This guide was adapted from Digital Ocean's tutorial [How To Serve Django Applications with Apache and mod_wsgi on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04).

#### Install the necessary software

	sudo apt-get update

	sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

#### Configure a Python Virtual Environment

At this point you should be in directory: **`<project-folder-name>`**
	
This allows us to keep the tools (Python modules) our project needs separate from our base Python installation.
 
**Install virtualenv**

Type into the terminal:

	sudo pip3 install virtualenv
 
**Create a Python virtual environment**

Type into the terminal:

  virtualenv <virtual-env-name>

##### Activate the Virtual Environment

  source <virtual-env-name>/bin/activate

Your terminal should output something like this:

  (myProjectEnv)user@host:~/myproject$.

While inside the virtual environment, type:

  pip install django

Deactivate the virtual environment by typing:

  deactivate

############################################################
############################################################


	

#### Configure Apache

To configure our Django app to be served by Apache, we'll need to edit the default virtual host file:
 
  sudo nano /etc/apache2/sites-available/000-default.conf

First we tell Apache to map any requests for `/static` to our project's static files folder.

  <VirtualHost *:80>
    
    ...
    
    Alias /static /home/ubuntu/<project-folder-name>/static
    
    <Directory  /home/ubuntu/<project-folder-name>/static>
      
      Require all granted
    
    </Directory>

  </VirtualHost>

 
This will allow our templates to access the required CSS and JavaScript files stored inside.
 
Next, we grant Apache access to the `wsgi.py` file, which is located at `/home/ubuntu/<project-folder-name>/inertia7/wsgi.py`
 
  <VirtualHost *:80>

    ...

    Alias /static /home/ubuntu/<project-folder-name>/static
    
    <Directory /home/ubuntu/<project-folder-name>/static>
    
      Require all granted
    
    </Directory>

    <Directory /home/ubuntu/<project-folder-name>/inertia7>
      
      <Files wsgi.py>
        
        Require all granted
      
      </Files>
    
    </Directory>

  </VirtualHost>

Lastly, specify the process group:

  <VirtualHost *:80>

    ...

    Alias /static /home/ubuntu/<project-folder-name>/static

    <Directory /home/ubuntu/<project-folder-name>/static>

      Require all granted

    </Directory>

    <Directory /home/ubuntu/<project-folder-name>/inertia7>
      
      <Files wsgi.py>

        Require all granted

      </Files>

    </Directory>

    WSGIDaemonProcess myproject python-path=/home/ubuntu/<project-folder-name>:/home/ubuntu/<project-folder-name>/<virtual-env-name>/lib/python3.4/site-packages

    WSGIProcessGroup myproject

    WSGIScriptAlias / /home/ubuntu/<project-folder-name>/inertia7/wsgi.py

  </VirtualHost>

**Remember**: Substitute python3.4 for whatever version of Python happens to be installed in `<virtual-env-name>`
 
#### Give Apache permission to access our project files:
  
  cd /home/ubuntu/<project-folder-name>

Give the group owner of database permissions to read/write the databse

  chmod 664 db.sqlite3
 
Then give the group Apache runs under ownership of the file

  sudo chown :www-data db.sqlite3
 
Lastly, restart Apache:

  sudo service apache2 restart
 
If everything was done correctly, we should now be able to view our website.
 
#### Debugging

Apache server error logs are stored in `/var/log/apache2/error.log`.
 
If you get a '500 - Interal Server Error' it is most likely caused by an error in the Django application. Read the error logs to find out more.


## ADMIN SETTINGS

The admin site contains the forms to create new users, projects, etcetera.


### Prerequisite: Create a superuser

From the command line, type:

    python manage.py createsuperuser

You will then be prompted to enter a username, email and password.


### Using the Admin Site
Go to http://(site this app is hosted on)/admin/ and sign in with your credentials.
