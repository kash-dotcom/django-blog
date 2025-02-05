from django.views import generic
from .models import AboutMe

# Create your views here.


class AboutList(generic.ListView):
    queryset = AboutMe.objects.all()
    template_name = "about/about.html"
