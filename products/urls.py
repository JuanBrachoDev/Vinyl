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
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]
