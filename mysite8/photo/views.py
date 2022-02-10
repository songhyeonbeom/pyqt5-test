from django.views.generic import ListView, DetailView
from photo.models import Album, Photo
from django.shortcuts import render


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


def index(request):
    """
    photo 목록 출력
    """

    return render(request, 'photo/album_list.html')
