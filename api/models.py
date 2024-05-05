from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class HoustonUser(AbstractUser):
    first_name = models.CharField(max_length=150, validators=[
        MinLengthValidator(3, message='First name must have at least 3 characters'),
        RegexValidator(r'^[a-zA-Z]*$', message='First name must contain only alphabets')
    ])
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
