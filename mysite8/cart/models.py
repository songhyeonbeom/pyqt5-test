from django.db import models
from django.contrib.auth.models import User
from photo.models import Photo
from datetime import datetime


class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = f'{verbose_name} 목록'

    @property
    def sub_total(self):
        return self.photo.price * self.quantity

    def __str__(self):
        return self.photo.name