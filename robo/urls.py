from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index_url"),
    path('feedbacks/',views.feedback_list_func, name='feedback_list_url'),
    path('interactions/',views.interactions_list_func, name='interactions_list_url')
]