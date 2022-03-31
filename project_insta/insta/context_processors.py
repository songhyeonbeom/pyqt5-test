from .models import Photo, Album


def menu_links(request):
    # select * from Ablum
    customer = request.user.id
    print(request)
    # select username, id from Album where owner_id='1' or
    links = Album.objects.filter(owner_id=customer)
    return dict(links = links)





def menu_links2(request) :
    links2 = Photo.objects.all()
    return dict(links2 = links2)
