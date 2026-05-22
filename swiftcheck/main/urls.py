from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course, name='courses'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
    
    path('api/courses/', views.api_courses, name='api_courses'),
    path('api/courses/<int:id>/', views.api_course_detail, name='api_course_detail'),
]