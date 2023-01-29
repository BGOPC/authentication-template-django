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


def course_tumb_directory_path(instance, filename):
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


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    shoppers = models.ManyToManyField(User, related_name='shopper')
    tumb = models.ImageField(upload_to=course_tumb_directory_path, null=False)
    lastUpdate = models.DateTimeField(auto_now=True)
    price = models.DecimalField(null=False, default=1000000, max_digits=7, decimal_places=0)


class Seller(User):
    address = models.CharField(max_length=255, null=False, default='')
    products = models.ManyToManyField(Product)


class Teacher(User):
    TOPICS = [
        ("BP", "Basic Programming"),
        ("AP", "Advanced Programming"),
        ("CS", "Computer Science"),
        ("MS", "Mathematics"),
        ("CH", "Chemistry"),
        ("BL", "BioLogy"),
        ("PH", "physics"),
        ("EL", "Electronics"),
        ("RG", "Religious"),
        ("Or", "Other"),
    ]
    topic = models.CharField(max_length=2, choices=TOPICS, default=TOPICS[-1][0])


class Course(Product):
    video = models.FileField(upload_to=course_directory_path, null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)


class Trip(models.Model):
    name = models.CharField(null=False, default='', max_length=150)
    date = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=1))
    members = models.ManyToManyField(User, related_name='members')
    price = models.DecimalField(null=False, default=1000000, max_digits=7, decimal_places=0)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                limit_choices_to={'is_staff': True}, related_name='manager')


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_announced = models.BooleanField(default=False, null=False)
    is_ticket = models.BooleanField(default=False, null=False)
    img = models.ImageField(upload_to=user_directory_path, null=True)
