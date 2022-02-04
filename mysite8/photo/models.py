from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField


class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('상품 제목', max_length=30)
    money = models.CharField('상품 가격', max_length=10)
    season = models.CharField('상품 시즌', max_length=20)
    style = models.TextField('스타일', blank=True)
    size = models.TextField('사이즈', blank=True)
    Material = models.TextField('소재', blank=True)
    image = ThumbnailImageField('상품 사진', upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)
    stock = models.IntegerField('재고 수량')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='작성자', blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

