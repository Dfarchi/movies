# Generated by Django 4.1.5 on 2023-01-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0008_rename_actor_movie_actors_remove_actor_roll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_actor',
            name='main_role',
            field=models.BooleanField(null=True),
        ),
    ]