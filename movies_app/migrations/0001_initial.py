# Generated by Django 4.1.5 on 2023-01-23 20:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(db_column='movie_name', max_length=256)),
                ('description', models.TextField(db_column='description')),
                ('duration', models.FloatField(db_column='duration')),
                ('pic_url', models.URLField(db_column='pic_url', max_length=512, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(db_column='rating', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='movies_app.movie')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
    ]