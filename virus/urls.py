from django.contrib import admin
from django.urls import path, include
from virus import views

urlpatterns = [
    path('', views.main, name="main"),
    path('about/', views.about, name="about"),
    path('hospital/', views.hospital, name="hospital"),
    path('patient/', views.patient, name="patient"),
    path('virus/', views.virus, name="virus"),
    path('community/', views.community, name="community"),
    path('posting/', views.create_posting, name="posting"),
    path('community/<int:id>', views.detail, name="detail"),
]
