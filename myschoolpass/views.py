from django.shortcuts import render, get_object_or_404
from .models import Course, Professor, Student
from django.contrib.auth.decorators import login_required

# login view
def login(request):
    return render(request, 'login.html')

# login view
def welcome(request):
    return render(request, 'index.html')

# course views
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

# User profile views
@login_required
def professor_profile(request, user_id):
    professor = get_object_or_404(Professor, user_id=user_id)
    return render(request, 'professor_profile.html', {'professor': professor})

@login_required
def student_profile(request, user_id):
    student = get_object_or_404(Student, user_id=user_id)
    return render(request, 'student_profile.html', {'student': student})
