# Generated by Django 3.2 on 2021-10-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211005_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='special_offer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]