from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower, Least

from .models import Album, Artist
from .forms import AlbumForm, ArtistForm


def all_albums(request):
    """ A view to show all albums, including sorting and search queries """

    albums = Album.objects.all().order_by('name')
    query = None
    sort = None
    category = None
    direction = None

    if request.GET:
        if 'genre' in request.GET:
            genre = request.GET['genre']
            albums = albums.filter(genre=genre)

        if 'category' in request.GET:
            category = request.GET['category']

            if category == 'deals':
                albums = albums.filter(special_offer_category='deal')

            if category == 'arrivals':
                albums = albums.filter(special_offer_category='new_arrival')

            if category == 'clearance':
                albums = albums.filter(special_offer_category='clearance')

            if category == 'specials':
                albums = albums.filter(~Q(special_offer_category='no_offer'))

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                albums = albums.annotate(lower_name=Lower('name'))

            if sortkey == 'artist':
                sortkey = 'lower_name'
                albums = albums.annotate(lower_name=Lower('artist__name'))

            if sortkey == 'price':
                sortkey = 'lower_price'
                albums = albums.annotate(
                    lower_price=Least('price', 'special_offer_price'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            albums = albums.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('albums'))

            queries = Q(
                name__icontains=query) | Q(
                    genre__icontains=query) | Q(
                        artist__name__icontains=query)
            albums = albums.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'albums': albums,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/albums.html', context)


def album_detail(request, album_id):
    """ A view to display the details of a single album. """

    album = get_object_or_404(Album, pk=album_id)

    context = {
        'album': album,
    }

    return render(request, 'products/album_detail.html', context)


def all_artists(request):
    """ A view to show all artists, including sorting queries """

    artists = Artist.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                artists = artists.annotate(lower_name=Lower('name'))

            if sortkey == 'featured':
                sortkey = 'name'
                artists = artists.filter(is_featured_artist=True)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artists = artists.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artists': artists,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/artists.html', context)


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


@login_required
def add_album(request):
    """ Add an album to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            messages.success(request, 'Successfully added album!')
            return redirect(reverse('album_detail', args=[album.id]))
        else:
            messages.error(request, 'Failed to add album. Please ensure the form is valid.')
    else:
        form = AlbumForm()

    template = 'products/add_album.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_artist(request):
    """ Add an artist to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Successfully added artist!')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to add artist. Please ensure the form is valid.')
    else:
        form = ArtistForm()

    template = 'products/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_album(request, album_id):
    """ Edit an album in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated album!')
            return redirect(reverse('album_detail', args=[album.id]))
        else:
            messages.error(request, 'Failed to update album. Please ensure the form is valid.')
    else:
        form = AlbumForm(instance=album)
        messages.info(request, f'You are editing {album.name}')

    template = 'products/edit_album.html'
    context = {
        'form': form,
        'album': album,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """ Edit an artist in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated album!')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to update artist. Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.name}')

    template = 'products/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)


@login_required
def delete_album(request, album_id):
    """ Delete an album from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    messages.success(request, 'Album deleted!')
    return redirect(reverse('albums'))


@login_required
def delete_artist(request, artist_id):
    """ Delete an artist from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    messages.success(request, 'Artist deleted!')
    return redirect(reverse('artists'))
