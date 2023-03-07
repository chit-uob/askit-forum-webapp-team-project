from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.poll_home, name='poll_home'),
]