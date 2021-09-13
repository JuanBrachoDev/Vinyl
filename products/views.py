from django.shortcuts import render, get_object_or_404
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


def album_detail(request, album_id):
    """ A view to display the details of a single album. """

    album = get_object_or_404(Album, pk=album_id)

    context = {
        'album': album,
    }

    return render(request, 'products/album_detail.html', context)