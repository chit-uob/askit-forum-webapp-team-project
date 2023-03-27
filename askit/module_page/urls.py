from django.urls import path
from . import views


app_name = 'module_page'
urlpatterns = [
    path('list/', views.view_module_list, name='module_list'),
    path('<str:mod>/', views.view_question_list, name='module'),
]