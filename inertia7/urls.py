"""inertia7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [ 
    url(r'^$', views.HomePageView.as_view()),
    url(r'^resources/', views.SimpleView.as_view(template_name="resources.html")),
    url(r'^admin/', admin.site.urls),
]

## Get a list of all our projects
from projects.models import Project
projects = Project.objects.all()
# End list

# Auto-route Projects
for project in projects:
    urlpatterns.append(url(r'^projects/' + project.url, views.ProjectView.as_view()))