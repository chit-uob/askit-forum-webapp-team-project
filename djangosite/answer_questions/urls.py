from django.urls import path
from . import views

app_name = 'answer_questions'
urlpatterns = [
    path('', views.index, name='index'),
]