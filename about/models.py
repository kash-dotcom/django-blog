from django.db import models
# from django.contrib.auth.models import User
# from django.contrib import admin

# Create your models here.


class AboutMe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

