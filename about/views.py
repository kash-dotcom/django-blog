from django.views import generic
from .models import AboutMe


class AboutDetail(generic.DetailView):
    model = AboutMe
    template_name = "about/about.html"

    def get_object(self):
        return AboutMe.objects.first()
