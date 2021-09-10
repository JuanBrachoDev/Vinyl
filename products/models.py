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
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to=get_artist_upload_path, null=True, blank=True)

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
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to=get_album_upload_path, null=True, blank=True)

    def __str__(self):
        return self.name
