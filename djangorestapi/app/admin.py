from django.contrib import admin
from . models import Album, Project, Song

admin.site.register(Project)
admin.site.register(Album)
admin.site.register(Song)