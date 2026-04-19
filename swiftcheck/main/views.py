from django.shortcuts import redirect, render
from .models import Course, User, User
from utils.forms import LoginForm, SignUpForm

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
    
    form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                confirm_password = confirm_password
            )

            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'main/signup.html', {'form': form})


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