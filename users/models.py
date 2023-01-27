from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_{instance.user.id}/%Y/%m/%d/{filename}'


class Group(models.Model):
    name = models.CharField(max_length=100, null=False, default='basic')


class User(AbstractUser):
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    group = models.ManyToManyField(Group)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    msg = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_announced = models.BooleanField(default=False, null=False)
    is_ticket = models.BooleanField(default=False, null=False)
    img = models.ImageField(upload_to=user_directory_path, null=True)
