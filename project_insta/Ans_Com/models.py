from django.db import models
from django.urls import reverse
from insta.fields import ThumbnailImageField
from common.models import User
from insta.models import Photo





class Answer(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_answer')
    voter = models.ManyToManyField(User, related_name='voter_answer')




