from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name  = models.CharField(max_length= 250, blank=False, default="")
    last_name  = models.CharField(max_length= 250, blank=False, default="")
    email = models.EmailField(max_length = 254, blank = False, null = False, default="")
    date_of_birth = models.DateTimeField()
    bvn = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name
        