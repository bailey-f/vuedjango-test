# Generated by Django 3.1.3 on 2021-07-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210709_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
