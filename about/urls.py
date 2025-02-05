from . import views
from django.urls import path

urlpatterns = [
    path('', views.AboutDetail.as_view(), name='about'),
]
