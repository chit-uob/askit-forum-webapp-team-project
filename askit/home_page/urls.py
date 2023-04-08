from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns = [
    path('notifs/', views.view_notifications, name='all_notifications'),
]