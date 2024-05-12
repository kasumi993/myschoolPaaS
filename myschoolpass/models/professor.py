from django.db import models
from django.contrib.auth.models import User
from myschoolpass.models.course import Course

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    courses_taught = models.ManyToManyField(Course, related_name='instructor', blank=True)

    def __str__(self):
        return self.user.username
