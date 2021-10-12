# Generated by Django 3.2 on 2021-10-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_first_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
