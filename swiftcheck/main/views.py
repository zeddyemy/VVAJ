from django.shortcuts import redirect, render
from .models import Course, User, User
from utils.forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'main/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('home')
        
        if not user:
            form = LoginForm(request.POST)
            form.add_error(None, 'Invalid username or password.')
            return render(request, 'main/login.html', {'form': form})
    
    form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if len(username) < 3:
                form.add_error('username', 'Username must be at least 3 characters long.')
                return render(request, 'main/signup.html', {'form': form})
            
            if email and User.objects.filter(email=email).exists():
                form.add_error('email', 'Email is already in use.')
                return render(request, 'main/signup.html', {'form': form})
     
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match.')
                
                return render(request, 'main/signup.html', {'form': form})
            
            
            
            #TODO: Check if password is strong enough; (it must have number, caps, small letter, special character and be at least 8 characters long)
            # ASSIGNMENT
            if len(password) < 8:
                form.add_error('password', 'Password must be at least 8 characters long.')
                return render(request, 'main/signup.html', {'form': form})
            
            
                
            if not any(char.isdigit() for char in password):
                form.add_error('password', 'Password must contain at least one number.')
                return render(request, 'main/signup.html', {'form': form})

            if not any(char.isupper() for char in password):
                form.add_error('password', 'Password must contain at least one uppercase letter.')
                return render(request, 'main/signup.html', {'form': form})

            if not any(char.islower() for char in password):
                form.add_error('password', 'Password must contain at least one lowercase letter.')
                return render(request, 'main/signup.html', {'form': form})

            if not any(char in '!@#$%^&*()-+' for char in password):
                form.add_error('password', 'Password must contain at least one special character.')
                return render(request, 'main/signup.html', {'form': form})
            
            

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