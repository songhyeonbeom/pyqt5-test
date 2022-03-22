from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)



class UserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            address = address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, address, password):
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
            address = address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=20, unique=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
    )
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'date_of_birth' ,'address', ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin