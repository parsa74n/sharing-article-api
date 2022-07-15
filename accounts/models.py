from .manager import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """
    custom user model. 
    """


    phone_number = models.CharField(max_length=11, unique=True) #we use this field for authentication
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()  #custom manager


    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    FEMALE = 1
    MALE = 2
    GENDER_NOT_PROVIDED = 3

    GENDER = ((FEMALE, 'female'), (MALE, 'male'), (GENDER_NOT_PROVIDED, '_'))
    gender = models.PositiveSmallIntegerField(default=3, choices=GENDER)

    def __str__(self):
        return f'{self.username} -- {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser
