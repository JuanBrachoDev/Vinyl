from django.contrib import admin
from .models import Album, Artist

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'artist',
        'genre',
        'price',
        'rating',
        'spotify_link',
        'image',
    )

    ordering = ('name',)

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image'
    )

    ordering = ('name',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)