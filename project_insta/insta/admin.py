# Register your models here.
from django.contrib import admin
from insta.models import Album, Photo, Answer


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'slug',)
    search_fields = ['name']



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt',)
    search_fields = ['title', 'slug', ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'content', 'create_date', 'owner']
    list_display_links = ['content', 'create_date']


