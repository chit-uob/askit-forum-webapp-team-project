from django.urls import path
from . import views

app_name = 'module_page'
urlpatterns = [
    path('', views.view_question_list, name='module'),
]