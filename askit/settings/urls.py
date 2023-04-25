from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('delete_account/', views.delete_account, name='delete_account'),
    path('change_username/', views.change_username, name='change_username')
]
