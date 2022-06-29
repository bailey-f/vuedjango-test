from django.db import models
from django.db.models.fields import DateField
from django.core.files import File

class Project(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    todo = models.TextField()
    isdone = models.BooleanField()
    notes = models.TextField()
    slug = models.SlugField()
    host = models.URLField(null=True, blank=False)
    img = models.ImageField(upload_to="upload/", null=True, blank=True)
    date = models.DateField(null=True, blank=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.title

    @property    
    def absolute_url(self):
        return f'/{self.slug}/'

class Album(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    artist = models.CharField(max_length=100)
    img = models.ImageField(upload_to="upload/", null=True, blank=False)
    host = models.URLField(null=True, blank=False)
    date = models.DateField(null=True, blank=False)
    primcolourR = models.IntegerField()
    primcolourG = models.IntegerField()
    primcolourB = models.IntegerField()
    accentcolourR = models.IntegerField()
    accentcolourG = models.IntegerField()
    accentcolourB = models.IntegerField()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.title

    @property    
    def absolute_url(self):
        return f'/{self.slug}/'

class Song(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    tracklist = models.IntegerField(null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    host = models.URLField(null=True, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album")

    def __str__(self):
        return self.title

    @property    
    def absolute_url(self):
        return f'/{self.album.slug}/{self.slug}/'
