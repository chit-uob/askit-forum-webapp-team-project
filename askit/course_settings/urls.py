from django.urls import path
from . import views

app_name = 'course_settings'
urlpatterns = [
    path('details/<str:mod>/', views.get_details, name='details'),
    path('update/<str:mod>/', views.update_details, name='update'),
]