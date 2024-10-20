from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.CharField(max_length=250, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to = "courses/%Y/%m/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject