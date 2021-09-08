from django.shortcuts import render
from .models import Album

# Create your views here.

def all_albums(request):
    """ A view to show all albums, including sorting and search queries """

    albums = Album.objects.all()

    context = {
        'albums': albums,
    }

    return render(request, 'products/albums.html', context)