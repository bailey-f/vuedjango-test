# Generated by Django 3.1.3 on 2021-07-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210707_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imgThumb',
            field=models.ImageField(default='..media/makingmovies.jpg', null=True, upload_to='../media/'),
        ),
    ]
