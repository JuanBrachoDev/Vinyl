# Generated by Django 3.2 on 2021-09-29 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210924_0652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='line_item_total',
            new_name='lineitem_total',
        ),
    ]
