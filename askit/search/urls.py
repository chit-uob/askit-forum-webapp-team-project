from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('normal/', views.search_all_modules, name='search_all_modules'),
    path('advanced/', views.advanced_search, name='advanced_search')
]