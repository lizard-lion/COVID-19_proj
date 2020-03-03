from django.contrib import admin
from django.urls import path, include
from virus import views

urlpatterns = [
    path('', views.main, name="main"),
]
