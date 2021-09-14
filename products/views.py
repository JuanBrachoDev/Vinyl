from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Album, Artist
from django.db.models.functions import Lower

# Create your views here.


def all_albums(request):
    """ A view to show all albums, including sorting and search queries """

    albums = Album.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                albums = albums.annotate(lower_name=Lower('name'))

            if sortkey == 'artist':
                sortkey = 'lower_name'
                albums = albums.annotate(lower_name=Lower('artist__name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            albums = albums.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('albums'))

            queries = Q(name__icontains=query) | Q(genre__icontains=query) | Q(artist__name__icontains=query)
            albums = albums.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'albums': albums,
        'search_term': query,
        'current_sorting': current_sorting,
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


def artist_detail(request, artist_id):
    """ A view to display the details of a single artist. """

    all_albums = Album.objects.all()

    artist = get_object_or_404(Artist, pk=artist_id)
    albums = all_albums.filter(artist=artist.id)

    context = {
        'artist': artist,
        'albums': albums,
    }

    return render(request, 'products/artist_detail.html', context)
