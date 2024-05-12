from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myschoolpass.models.professor import Professor
from myschoolpass.models.student import Student
from myschoolpass.models.course import Course

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):
        # Create default courses
        course1, _ = Course.objects.get_or_create(
            title='Mathematics 101',
            defaults={
                'description': 'Basic Mathematics',
                'level': 'beginner',
                'available_seats': 30
            }
        )

        course2, _ = Course.objects.get_or_create(
            title='Physics 101',
            defaults={
                'description': 'Basic Physics',
                'level': 'beginner',
                'available_seats': 30
            }
        )

        # Create default professor user
        prof_user, created_prof = User.objects.get_or_create(
            username='professor',
            defaults={
                'first_name': 'Professor',
                'last_name': 'Default',
                'email': 'professor@example.com'
            }
        )
        if created_prof:
            prof_user.set_password('professor')
            prof_user.save()
            professor, _ = Professor.objects.get_or_create(
                user=prof_user,
                defaults={
                    'username': 'professor',
                    'first_name': 'Professor',
                    'last_name': 'Default',
                    'email': 'professor@example.com',
                    'password': 'professor'
                }
            )
            professor.courses_taught.add(course1, course2)
            self.stdout.write(self.style.SUCCESS('Successfully created professor user'))

        # Create default student user
        stud_user, created_stud = User.objects.get_or_create(
            username='student',
            defaults={
                'first_name': 'Student',
                'last_name': 'Default',
                'email': 'student@example.com'
            }
        )
        if created_stud:
            stud_user.set_password('student')
            stud_user.save()
            student, _ = Student.objects.get_or_create(
                user=stud_user,
                defaults={
                    'username': 'student',
                    'first_name': 'Student',
                    'last_name': 'Default',
                    'email': 'student@example.com',
                    'password': 'student'
                }
            )
            student.courses_enrolled.add(course1, course2)
            self.stdout.write(self.style.SUCCESS('Successfully created student user'))
