from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from . models import Project, Album, Song
from . serializers import ProjectSerializer, AlbumSerializer, SongSerializer

class ProjectsView(generics.RetrieveAPIView):
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

class ProjectView(APIView):

    def get_object(self, projectslug):
        try:
            return Project.objects.get(slug=projectslug)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, projectslug, format=None):
        queryset = self.get_object(projectslug)
        serializer = ProjectSerializer(queryset)
        return Response(serializer.data)


class AlbumsView(generics.RetrieveAPIView):
    queryset = Album.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

class AlbumView(APIView):

    def get_object(self, albumslug):
        try:
            return Album.objects.get(slug=albumslug)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, albumslug, format=None):
        queryset = self.get_object(albumslug)
        serializer = AlbumSerializer(queryset)
        return Response(serializer.data)

class SongView(generics.RetrieveAPIView):
    queryset = Song.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data)