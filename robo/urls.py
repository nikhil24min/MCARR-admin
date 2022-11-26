from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index_url"),
    path("register/", views.register_request, name="register_url"),
    path("login", views.login_request, name="login_url"),
    path("logout", views.logout_request, name= "logout_url"),


    path('feedbacks/',views.feedback_list_func, name='feedback_list_url'),
    path('interactions/',views.interactions_list_func, name='interactions_list_url'),
    path("chatbot", views.chatbot_func, name= "chatbot_url"),
]