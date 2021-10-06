from django.db import models
import os


# Artist banner upload path method, applies lowercase and replaces
# spaces with underscores.
def get_artist_upload_path(instance, filename):
    return os.path.join(
        f'products/{instance.name}'.lower().replace(" ", "_"), filename)


# Album cover upload path method, applies lowercase and replaces
# spaces with underscores.
def get_album_upload_path(instance, filename):
    return os.path.join(
        f'products/{instance.artist}/{instance.name}'.lower().replace(
            " ", "_"), filename)


# Artist model
class Artist(models.Model):

    class Meta:
        verbose_name_plural = 'Artists'

    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to=get_artist_upload_path, null=True, blank=True)
    is_featured_artist = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Album model
class Album(models.Model):

    class Meta:
        verbose_name_plural = 'Albums'

    artist = models.ForeignKey('Artist', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    spotify_link = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to=get_album_upload_path, null=True, blank=True)

    offers = (
        ('no_offer', 'No Offer'),
        ('new_arrival', 'New Arrival'),
        ('deal', 'Deal'),
        ('clearance', 'Clearance'),
    )

    special_offer_category = models.CharField(max_length=254, choices=offers, default='no_offer')
    special_offer_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
