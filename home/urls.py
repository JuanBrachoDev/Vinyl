from django.contrib import admin
from django.urls import path
from . import views

# Home app urls
urlpatterns = [
    path('', views.index, name='home')
]
