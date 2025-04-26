from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser, UserManager , PermissionsMixin
from django.contrib.auth.models import User
# Create your models here.

class Customer(User):

    phone_number = models.CharField(max_length=11,unique=True)
