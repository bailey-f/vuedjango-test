# Generated by Django 3.1.3 on 2021-07-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210707_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='accentcolour',
        ),
        migrations.RemoveField(
            model_name='album',
            name='primcolour',
        ),
        migrations.AddField(
            model_name='album',
            name='accentcolourB',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='accentcolourG',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='accentcolourR',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='primcolourB',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='primcolourG',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='primcolourR',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
