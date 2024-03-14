from django.db import models
from django.contrib.auth.models import AbstractUser

# customer
class CustomUser(AbstractUser):
    location = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
