from django.urls import path, include
from . import views


app_name = 'module_page'
urlpatterns = [
    path('list/', views.view_module_list, name='module_list'),
    path('<str:mod>/', views.view_question_list, name='all_questions'),
    path('<str:mod>/popular/<int:days>', views.view_popular_questions, name='popular_questions'),
    path('<str:mod>/admin', views.is_admin,name='is_admin'),
    path('<str:mod>/getUsers', views.get_all_users,name='get_Users'),
    path('<str:mod>/updateRoles', views.update_roles,name='update_role'),
    path('<str:mod>/updateMembers', views.update_members,name='update_members'),
    path('<str:mod>/removeMembers', views.remove_members,name='remove_members'),
    path('<str:mod>/updateAdmins', views.update_admins,name='update_admins'),
    path('<str:mod>/removeAdmins', views.remove_admins,name='remove_admins'),
    path('<str:mod>/course-settings/', include('course_settings.urls')),
]