from django.contrib import admin
from account.models import User, CustomUser
# Register your models here.

admin.site.register(CustomUser)