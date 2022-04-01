from .models import Photo, Album


def menu_links(request):
    customer = request.user.id
    print(request)
    links = Album.objects.filter(owner_id=customer)
    return dict(links = links)





def menu_links2(request) :
    links2 = Photo.objects.all()
    return dict(links2 = links2)
