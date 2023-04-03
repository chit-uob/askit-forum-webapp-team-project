
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/question/', include('answer_questions.urls')),
    path('api/module/', include('module_page.urls')),
    path('api/ask/', include('ask_questions.urls')),
    path('api/search/', include('search.urls')),
    path('api/signup/',include('signup.urls')),
    path('api/create_module/', include('create_module.urls')),
    path('api/course-settings/', include('course_settings.urls')),
]
