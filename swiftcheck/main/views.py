from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')

def course(request):
    courses = Course.objects.all()
    # frontend_courses = Course.objects.filter(category='FRONTEND')
    # backend_courses = Course.objects.filter(category='BACKEND')
    # fullstack_courses = Course.objects.filter(category='FULLSTACK')
    print(courses)
    
    # print(frontend_courses)
    # print(backend_courses)
    # print(fullstack_courses)

    context = {
        'courses': courses,
        # 'frontend_courses': frontend_courses,
        # 'backend_courses': backend_courses,
        # 'fullstack_courses': fullstack_courses,
    }
    return render(request, 'main/course.html', context)

