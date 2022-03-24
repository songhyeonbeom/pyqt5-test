from django.urls import path
from insta import views, vote_views



app_name = 'insta'
urlpatterns = [


    path('', views.allPhotoAB, name='allPhotoAB'),

    path('<slug:c_slug>/', views.allPhotoAB, name='album_detail'),
    # path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),




    # Example: /insta/album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    # Example: /insta/album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # Example: /insta/album/99/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),

    # Example: /insta/album/99/delete/
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),

    # Example: /insta/insta/add/
    path('insta/add/', views.PhotoCV.as_view(), name='photo_add'),

    # Example: /insta/insta/change/
    path('insta/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # Example: /insta/insta/99/update/
    path('insta/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),

    # Example: /insta/insta/99/delete/
    path('insta/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),





    # path('photo/<int:pk>/', views.PhotoDV, name='photo_detail'),





    # path('id:c_slug/id:photo_slug', views.PhotoABDetail, name = 'PhotoABDetail'),

    # path('vote/photo/<int:photo_id>/', vote_views.vote_photo, name='vote_photo'),

]



