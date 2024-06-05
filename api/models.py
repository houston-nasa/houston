from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class HoustonUser(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(3, message="First name must have at least 3 characters"),
            RegexValidator(
                r"^[a-zA-Z]*$", message="First name must contain only alphabets"
            ),
        ],
    )
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }


class GithubToken(models.Model):
    user = models.ForeignKey(HoustonUser, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    token = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def json(self):
        return {
            "id": self.id,
            "token": self.token,
            "user": self.user.json(),
            "owner": self.owner,
        }


class GithubRepo(models.Model):
    user = models.ForeignKey(HoustonUser, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def json(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "user": self.user.json(),
            "repo": self.repo,
        }

    def __str__(self):
        return f"{self.owner}/{self.repo}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "repo"], name="unique_owner_repo")
        ]
