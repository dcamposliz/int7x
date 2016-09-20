from django.db import models

class Requirements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    show_on_front_page = models.BooleanField(default=True)
    url = models.CharField(max_length=200)
    cover_photo = models.CharField(max_length=100,blank=True,null=True)
    thumbnail_photo = models.CharField(max_length=100,blank=True,null=True)
    abstract = models.TextField()
    requirements = models.ForeignKey(Requirements,blank=True,null=True)
    contributors = models.CharField(max_length=400)
    content = models.TextField()
    github_link = models.URLField(blank=True,null=True)
    next_tutorial = models.ForeignKey('self',blank=True,null=True)
    
    def __str__(self):
        return "{0} ({1})".format(self.title,self.url)
        