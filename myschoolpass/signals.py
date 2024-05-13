from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
from .utils import publish_course_update

@receiver(post_save, sender=Course)
def course_updated(sender, instance, **kwargs):
    publish_course_update(instance)
