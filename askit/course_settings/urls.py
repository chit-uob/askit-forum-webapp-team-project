from django.urls import path
from . import views

app_name = 'course_settings'
urlpatterns = [
    path('', views.course_settings, name = "course_settings"),
]