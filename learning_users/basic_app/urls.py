from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('logged_in/',views.user_logged_in,name='logged_in'),
    path('user_login',views.user_login,name='user_login'),
]