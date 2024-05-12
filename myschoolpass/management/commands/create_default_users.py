from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myschoolpass.models import Professor, Student

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):
        # Create default professor user
        prof_user, created_prof = User.objects.get_or_create(username='professor')
        if created_prof:
            prof_user.set_password('professor')
            prof_user.save()
            Professor.objects.get_or_create(user=prof_user)
            self.stdout.write(self.style.SUCCESS('Successfully created professor user'))

        # Create default student user
        stud_user, created_stud = User.objects.get_or_create(username='student')
        if created_stud:
            stud_user.set_password('student')
            stud_user.save()
            Student.objects.get_or_create(user=stud_user)
            self.stdout.write(self.style.SUCCESS('Successfully created student user'))
