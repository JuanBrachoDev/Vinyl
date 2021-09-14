from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.all_albums, name='albums'),
    path('albums/<album_id>/', views.album_detail, name='album_detail'),
    path('artists/', views.all_artists, name='artists'),
    path('artists/<artist_id>/', views.artist_detail, name='artist_detail'),
]
