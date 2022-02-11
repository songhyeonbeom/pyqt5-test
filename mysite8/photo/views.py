from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo, Test
from django.shortcuts import render
import json

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

def addprice(request):
    # print(request.body)
    jsonObject = json.loads(request.body)
    # print(jsonObject)
    # print(jsonObject["price"])
    test = Test()
    test.price = jsonObject["price"]
    test.save()

    return HttpResponse("true", content_type='application/json')