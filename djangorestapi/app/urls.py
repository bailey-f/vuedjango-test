from django.urls import path
from django.views.generic.base import TemplateView
from . views import ProjectsView, AlbumView, SongView, AlbumsView, ProjectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects_view'),
    path('projects/<slug:projectslug>/', ProjectView.as_view(), name='project_view'),
    path('albums/', AlbumsView.as_view(), name='albums_view'),
    path('albums/<slug:albumslug>/', AlbumView.as_view(), name='album_view'),
    path('songs/', SongView.as_view(), name='song_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)