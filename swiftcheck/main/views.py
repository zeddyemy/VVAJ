from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')

def course(request):
    courses = Course.objects.all()
    print(courses)
    
    context = {
        'courses': courses
    }
    return render(request, 'main/course.html', context)