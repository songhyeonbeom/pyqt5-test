# Register your models here.
from django.contrib import admin
from insta.models import Album, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description', 'slug')
    prepopulated_fields = {'slug' : ('name',)}



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt', 'slug')
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 20

