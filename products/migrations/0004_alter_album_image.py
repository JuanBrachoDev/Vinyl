# Generated by Django 3.2 on 2021-09-09 09:01

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210909_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.get_album_upload_path),
        ),
    ]
