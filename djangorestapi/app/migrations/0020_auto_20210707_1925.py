# Generated by Django 3.1.3 on 2021-07-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210707_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='img',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='imgThumb',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]
