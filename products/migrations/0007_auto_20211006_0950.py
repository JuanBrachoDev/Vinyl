# Generated by Django 3.2 on 2021-10-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_album_special_offer_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='description',
        ),
        migrations.AddField(
            model_name='artist',
            name='is_featured_artist',
            field=models.BooleanField(default=False),
        ),
    ]
