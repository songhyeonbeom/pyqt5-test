from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='아이디')
    user_pw = models.CharField(max_length=128, verbose_name='비밀번호')
    user_name = models.CharField(max_length=16, unique=True, verbose_name='이름')
    user_email = models.EmailField(max_length=128, unique=True, verbose_name='이메일')
    user_number = models.CharField(max_length=20, unique=True, verbose_name='휴대전화')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')



    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'

    def __str__(self):
        return self.user_name


