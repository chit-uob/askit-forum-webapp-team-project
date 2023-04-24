from django.urls import path
from . import views

app_name = 'course_settings'
urlpatterns = [
    path('details/<str:mod>', views.get_details, name='details'),
]