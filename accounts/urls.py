from django.urls import path
from . import views

app_name = 'AppAccountsName'

urlpatterns = [
    path('signup', views.signup_view, name="PathSignupName"),
    path('login', views.login_view, name='PathLoginName'),
    path('logout', views.logout_view, name='PathLogoutName'),
]
