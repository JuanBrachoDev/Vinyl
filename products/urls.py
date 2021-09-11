from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.all_albums, name='albums'),
    path('artists/', views.all_artists, name='artists')
]