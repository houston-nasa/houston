from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import HoustonUser

# Register your models here.
admin.site.register(HoustonUser, UserAdmin)
