import datetime

from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_{instance.author.id}/%Y/%m/%d/{filename}'


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
    is_seller = models.BooleanField(default=False, null=False)
    is_teacher = models.BooleanField(default=False, null=False)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password"]

    def save(self, *args, **kwargs):
        self.username = slugify(self.first_name + self.last_name)
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    students = models.ManyToManyField(User)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    lastUpdate = models.DateTimeField(auto_add=True)
    price = models.DecimalField(null=False, default=1000000)


class Trip(models.Model):
    name = models.CharField(null=False, default='', max_length=150)
    date = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=1))
    members = models.ManyToManyField(User)
    price = models.DecimalField(null=False, default=1000000)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_announced = models.BooleanField(default=False, null=False)
    is_ticket = models.BooleanField(default=False, null=False)
    img = models.ImageField(upload_to=user_directory_path, null=True)
