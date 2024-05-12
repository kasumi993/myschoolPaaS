from django.contrib import admin
from myschoolpass.models import Course, Professor, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'instructor', 'available_seats', 'expiration_date')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)
