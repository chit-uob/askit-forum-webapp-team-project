from django.urls import path
from . import views


app_name = 'module_page'
urlpatterns = [
    path('list/', views.view_module_list, name='module_list'),
    path('<str:mod>/', views.view_question_list, name='all_questions'),
    path('<str:mod>/popular/<int:days>', views.view_popular_questions, name='popular_questions'),
]