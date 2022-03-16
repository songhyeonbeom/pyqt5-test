from django.db import models
from django.urls import reverse
# Create your models here.
from insta.fields import ThumbnailImageField


class Album(models.Model):
    #id 프라이머리키
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('insta:album_detail', args = [self.id])

    def __str__(self) :
        return '{}'.format(self.name)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField('IMAGE', upload_to='insta/%Y/%m')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('title',)
        # db_table- "Photo_table"
        # verbose_name = "my favorite post"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('insta:photo_detail', args = [self.id])
