# Generated by Django 4.1.5 on 2023-01-23 20:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0005_rating_rating_date_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(db_column='year', default=5, validators=[django.core.validators.MinValueValidator(1899), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
    ]