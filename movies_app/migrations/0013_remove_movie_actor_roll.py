# Generated by Django 4.1.5 on 2023-01-31 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0012_remove_actor_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_actor',
            name='roll',
        ),
    ]
