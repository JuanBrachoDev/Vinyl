from django.urls import path
from . import views

# Product urls
urlpatterns = [
    path('albums/', views.all_albums, name='albums'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('artists/', views.all_artists, name='artists'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_artist/', views.add_artist, name='add_artist'),
]
