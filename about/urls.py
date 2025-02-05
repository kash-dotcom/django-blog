from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.AboutList.as_view(), name='about'),
]
