from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_{instance.user.id}/%Y/%m/%d/{filename}'


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    join = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="profile/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.lastName}"


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    msg = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_announced = models.BooleanField(default=False, null=False)
    img = models.ImageField(upload_to=user_directory_path, null=True)
