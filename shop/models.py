import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import User


# Create your models here.
def course_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_courses_{instance.teacher.id}/%Y/%m/%d/{instance.name + "." + filename.split(".")[1]}'


def course_tumb_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_courses_{instance.teacher.id}/%Y/%m/%d/{instance.name + "." + filename.split(".")[1]}'


class BaseProduct(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100, null=False, blank=True)
    shoppers = models.ManyToManyField(User)
    tumb = models.ImageField(upload_to=course_tumb_directory_path, null=False, blank=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    price = models.DecimalField(null=False, default=1000000, max_digits=7, decimal_places=0)


class Product(BaseProduct):
    count = models.DecimalField(null=False, default=1, max_digits=7, decimal_places=0)


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


class Course(BaseProduct):
    video = models.FileField(upload_to=course_directory_path, null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='courses')


class Seller(User):
    address = models.CharField(max_length=255, null=False, default='')
    products = models.ManyToManyField(Product)


class Trip(models.Model):
    name = models.CharField(null=False, default='', max_length=150)
    date = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=1))
    members = models.ManyToManyField(User, related_name='members')
    price = models.DecimalField(null=False, default=1000000, max_digits=7, decimal_places=0)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                limit_choices_to={'is_staff': True}, related_name='manager')
