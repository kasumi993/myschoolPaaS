from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    available_seats = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title