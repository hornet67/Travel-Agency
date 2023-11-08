from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .manager import Custom_manager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    gender_choice = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    username = 'none'

    email = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)

    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=gender_choice)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    phone = models.CharField(max_length=11, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = Custom_manager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.phone
