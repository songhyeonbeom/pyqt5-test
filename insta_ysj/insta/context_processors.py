from .models import Photo, Album

def menu_links(request) :
    links = Album.objects.all()
    return dict(links = links)


def menu_links2(request) :
    links2 = Photo.objects.all()
    return dict(links2 = links2)