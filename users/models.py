from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_{instance.author.id}/%Y/%m/%d/{filename}'


def course_tumb_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_courses_{instance.teacher.id}/%Y/%m/%d/{instance.name + "." + filename.split(".")[1]}'


def course_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_courses_{instance.teacher.id}/%Y/%m/%d/{instance.name + "." + filename.split(".")[1]}'


class Group(models.Model):
    name = models.CharField(max_length=100, null=False, default='basic')


class User(AbstractUser):
    username = models.SlugField(default="", null=False, db_index=True, blank=True)  # forced by django admin problems :(
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    group = models.ManyToManyField(Group)
    is_teacher = models.BooleanField(default=False, null=False)
    is_seller = models.BooleanField(default=False, null=False)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password"]

    def save(self, *args, **kwargs):
        self.username = slugify(self.first_name + self.last_name)
        super().save(*args, **kwargs)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_announced = models.BooleanField(default=False, null=False)
    is_ticket = models.BooleanField(default=False, null=False)
    img = models.ImageField(upload_to=user_directory_path, null=True)
