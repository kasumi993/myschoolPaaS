from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    instructor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='courses_taught')
    students = models.ManyToManyField('Student', related_name='courses_enrolled', blank=True)
    available_seats = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title