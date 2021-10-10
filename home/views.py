from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower

from products.models import Album, Artist

# A view that shows the landing page
def index(request):
    """ A view to return the index page with some of the special
    deals and a list of all albums at the end. """

    all_albums = Album.objects.all()
    albums = all_albums.order_by('name')

    all_featured_artists = Artist.objects.filter(is_featured_artist=True)
    featured_artist_id = all_featured_artists.order_by('?')[:1][0].id
    featured_artist = all_featured_artists.filter(id=featured_artist_id)
    featured_artist_albums = all_albums.filter(artist=featured_artist_id).order_by('?')[:4]

    new_arrivals = all_albums.filter(special_offer_category='new_arrival').order_by('?')[:2]

    deals = all_albums.filter(special_offer_category='deal').order_by('?')[:4]

    clearances = all_albums.filter(special_offer_category='clearance').order_by('?')[:2]

    context = {
        'albums': albums,
        'featured_artist': featured_artist,
        'featured_artist_albums': featured_artist_albums,
        'new_arrivals': new_arrivals,
        'deals': deals,
        'clearances': clearances,
    }

    return render(request, 'home/index.html', context)
