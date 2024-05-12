from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Professor, Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
import logging

# Configure logger
logger = logging.getLogger(__name__)

# login view
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            try:
                if Professor.objects.filter(user=user).exists():
                    return redirect(f'/professors/{user.id}/')
                elif Student.objects.filter(user=user).exists():
                    return redirect(f'/students/{user.id}/')
            except Exception as e:
                logger.error(f"Error in redirecting: {e}")
                print(f"Error in redirecting: {e}")
        else:
            logger.warning(f"Invalid credentials for username: {username}")
            print(f"Invalid credentials")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
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
