from django.core.management.base import BaseCommand
from myschoolpass.subscriber import subscribe_to_course_updates

class Command(BaseCommand):
    help = 'Run Redis subscriber for course updates'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting Redis subscriber...'))
        subscribe_to_course_updates()
