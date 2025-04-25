from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser, UserManager , PermissionsMixin

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)