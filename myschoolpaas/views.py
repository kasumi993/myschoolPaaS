from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def loginPage(request):
    return render(request, "login.html")

def studentProfile(request):
    return render(request, "student-profile.html")

def teacherProfile(request):
    return render(request, 'teacher-profile.html')

def notifications(request):
    return render(request, 'notifications.html')
