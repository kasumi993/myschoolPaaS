from django.contrib import admin
from myschoolpass.models import Course, Professor, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'get_instructors', 'available_seats', 'expiration_date')
    search_fields = ('title', 'level')
    list_filter = ('level',)

    def get_instructors(self, obj):
        return ", ".join([professor.username for professor in obj.instructor.all()])
    get_instructors.short_description = 'Instructors'

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'get_courses')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('courses_taught__title',)

    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.courses_taught.all()])
    get_courses.short_description = 'Courses Taught'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'get_courses')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('courses_enrolled__title',)

    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.courses_enrolled.all()])
    get_courses.short_description = 'Courses Enrolled'

admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Student, StudentAdmin)
