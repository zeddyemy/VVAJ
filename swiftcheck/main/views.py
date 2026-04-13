from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')

def course(request):
    courses = Course.objects.all()
    frontend_courses = Course.objects.filter(category='FRONTEND')
    backend_courses = Course.objects.filter(category='BACKEND')
    fullstack_courses = Course.objects.filter(category='FULLSTACK')

    context = {
        'courses': courses,
        'frontend_courses': frontend_courses,
        'backend_courses': backend_courses,
        'fullstack_courses': fullstack_courses,
    }
    return render(request, 'main/course.html', context)

def course_detail(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'main/course_detail.html', context)