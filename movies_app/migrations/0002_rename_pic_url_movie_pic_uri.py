# Generated by Django 4.1.5 on 2023-01-23 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='pic_url',
            new_name='pic_uri',
        ),
    ]
