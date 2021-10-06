from django.contrib import admin
from .models import Album, Artist


# Admin display for Album
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'artist',
        'genre',
        'price',
        'rating',
        'spotify_link',
        'image',
        'special_offer_category',
        'special_offer_price',
    )

    ordering = ('name',)


# Admin display for Artist
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'is_featured_artist',
    )

    ordering = ('name',)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
