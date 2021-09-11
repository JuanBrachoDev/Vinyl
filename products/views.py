from django.shortcuts import render
from .models import Album, Artist

# Create your views here.


def all_albums(request):
    """ A view to show all albums, including sorting and search queries """

    albums = Album.objects.all()

    context = {
        'albums': albums,
    }

    return render(request, 'products/albums.html', context)


def all_artists(request):
    """ A view to show all artists, including sorting and search queries """

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'products/artists.html', context)