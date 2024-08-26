from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_page,name='logout')
]
