# Generated by Django 3.1.3 on 2021-07-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210708_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]