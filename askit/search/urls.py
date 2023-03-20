from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('all/', views.search_all_modules, name='search_all_modules'),
]