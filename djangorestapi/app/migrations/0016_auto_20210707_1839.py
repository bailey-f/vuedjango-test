# Generated by Django 3.1.3 on 2021-07-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_album_imgthumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='img',
            field=models.ImageField(default='makingmovies.jpg', null=True, upload_to='../media/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='imgThumb',
            field=models.ImageField(default='makingmovies.jpg', null=True, upload_to='../media/'),
        ),
    ]