from django.urls import path
from . import views

app_name = 'create_module'
urlpatterns = [
    path('new/', views.new_module, name='newModule'),
    path('delete/<str:mod>/', views.delete_module, name='deleteModule'),
]