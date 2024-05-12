from celery import shared_task
from django.utils import timezone
from .models import Course
from django.contrib.auth.models import User

@shared_task
def publish_course_update(course_id, update_type):
    course = Course.objects.get(pk=course_id)
    users = User.objects.filter(
        student__courses_enrolled=course
    ) | User.objects.filter(
        professor__courses_taught=course
    )

@shared_task
def expire_course():
    expired_courses = Course.objects.filter(
        expiration_date__lte=timezone.now()
    )
    for course in expired_courses:
        # Set course as expired
        course.available_seats = 0
        course.save()

        # Send notifications to instructors and students
        instructor = course.instructor.user
        students = [student.user for student in course.students.all()]

        # Send notification to instructor
        # (Implementation depends on your notification system)
        send_notification(
            recipient=instructor,
            message=f"The course '{course.title}' has expired."
        )

        # Send notifications to students
        for student in students:
            send_notification(
                recipient=student,
                message=f"The course '{course.title}' that you were enrolled in has expired."
            )