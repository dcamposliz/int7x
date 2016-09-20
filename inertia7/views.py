from django import template
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.utils.html import format_html
from django.http import HttpResponse
from django.http import HttpRequest

# Get a list of all our projects
from projects.models import Project
projects = Project.objects.all()

# Home page view
class HomePageView(TemplateView):
    template_name = "index.html"
    # This function passes a context to the template #
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
        # Add raw projects list to context
        context["projects"] = projects
        
	    # Modifying context passed to the template #
        return context

# Simple view (used for Resources)
class SimpleView(TemplateView):
    # This function passes a context to the template #
    def get_context_data(self, **kwargs):
        context = super(SimpleView, self).get_context_data(**kwargs)

	    # Modifying context passed to the template #
        return context
        
## Project view
# Used for grabbing the content of <h1> elements/creating the steps list #
from html.parser import HTMLParser
class HeaderGrabber(HTMLParser):
    def __init__(self):
        super(HeaderGrabber,self).__init__()
        self.read_header = False
        self.headers = []
    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self.read_header = True
    def handle_endtag(self, tag):
        if self.read_header:
            self.read_header = False
    def handle_data(self, data):
        if self.read_header:
            self.headers.append(data)        

# Used for replacing user-provided HTML code
class HTMLReplace(HTMLParser):
    def __init__(self,url):
        super(HTMLReplace,self).__init__()
        self.current_tag = None
        self.html_replace = ""
        
        # <h1> Counter
        self.h1_count = 0
        
        self.url = url
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        
        if self.current_tag == "h1":
            self.h1_count += 1
        
            # Add id="step1" to <h1> tags
            self.html_replace += "<h1 id='step{0}'>".format(self.h1_count)
            
            # Make <h1> a link
            self.html_replace += "<a href='#step{0}'>".format(self.h1_count)
        
        # Add section class attribute
        elif self.current_tag == "section":
            self.html_replace += "<section class='xlarge-paragraph'>"
        
        # Don't forget attribute tags!
        else:
            attributes = ""
            if attrs:
                for i in attrs:
                    # Append static file directory to img src
                    if self.current_tag == "img" and i[0] == "src":
                        img_src = "/static/{0}/{1}".format(self.url,i[1])
                        attributes += " {0}='{1}'".format(i[0],img_src)
                    else:
                        attributes += " {0}='{1}'".format(i[0],i[1])
            self.html_replace += "<{0}{1}>".format(tag,attributes)
    def handle_endtag(self, tag):
        if self.current_tag == "h1":
            self.html_replace += "</a></h1>"
        else:
            self.html_replace += "</{0}>".format(tag)
            
        self.current_tag = None
    def handle_data(self, data):
        # Add a counter (1, 2, 3, ...) before all <h1> tags
        if self.current_tag == "h1":
            self.html_replace += "{0}. {1}".format(self.h1_count,data)
        else: 
            self.html_replace += data
    # Return replaced HTML code when called
    def __call__(self):
        return self.html_replace
            
# Generic Project view
class ProjectView(TemplateView):
    template_name = "project.html"
    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        
        # Decide what project to load based on the url
        url = self.request.path.split("/")[2]
        context["project"] = Project.objects.filter(url=url)[0]
        proj = context["project"]
        
        # Subtitle magic
        proj.subtitle = bold_capitalized(proj.subtitle)
        
        # Meta-data
        context["meta_author"] = str(proj.contributors)
        
        # Cover Photo
        if proj.cover_photo:
            proj.cover_photo = "/static/{0}/{1}".format(url,proj.cover_photo)
        
        # Make Requirements text Django friendly (if defined)
        if proj.requirements_id:
            proj.requirements.content = format_html(proj.requirements.content)
        
        # Custom abstract styling
        temp = proj.abstract.replace("\n","</p><p>")
        proj.abstract = "<p>"
        proj.abstract += temp
        proj.abstract += "</p>"
        proj.abstract = format_html(proj.abstract)
        
        # Contributors field should be a comma separated list of authors
        proj.contributors = proj.contributors.split(",")
        
        ## Auto-generate steps from headers
        headers = HeaderGrabber()
        headers.feed(proj.content)
        context["headers"] = headers.headers
        
	    ## Custom content styling
        replace_content = HTMLReplace(url=url)
        replace_content.feed(proj.content)
        proj.content = format_html(replace_content())

        return context

## Used for subtitle
# Wrap <strong></strong> tags around any word that starts with a capital letter
# Or a number
def bold_capitalized(string):
    new = []
    for i in string.split(" "):
        if i[0].isupper() or i[0].isnumeric():
            new.append("<strong>{0}</strong>".format(i))
        else:
            new.append(i)
    return format_html(" ".join(new))