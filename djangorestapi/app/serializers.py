from rest_framework import serializers
from . models import Project, Album, Song

class ProjectSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField()

    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField()

    class Meta:
        model = Song
        fields = '__all__'