# Generated by Django 4.1.5 on 2023-01-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_rename_pic_url_movie_pic_uri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pic_uri',
            field=models.URLField(db_column='pic_uri', max_length=512, null=True),
        ),
    ]
