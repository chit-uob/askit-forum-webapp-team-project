from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns = [
    # path('', views.home_page, name='homePage'),
    # path('about/', views.about_page, name='aboutPage'),
    # path('contact/', views.contact_page, name='contactPage'),
    # path('faq/', views.faq_page, name='faqPage'),
    # path('privacy/', views.privacy_page, name='privacyPage'),
    # path('terms/', views.terms_page, name='termsPage'),
    path('notifs/', views.view_notifications, name='all_notifications'),
    path('activity/', views.view_activity, name='all_activity'),
    path('vQuestions/', views.view_questions, name='all_questions'),
    path('vAnswers/', views.view_answers, name='user_answers'),
    path('user_prof/', views.user_profiles, name='profile'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
]