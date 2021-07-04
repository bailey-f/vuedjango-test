from django.db import models
from django.db.models.fields import DateField

class Post (models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    host = models.URLField(null=True, blank=False)
    date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.title
