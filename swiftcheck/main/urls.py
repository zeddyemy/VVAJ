from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course, name='courses'),
    path('api/courses/', views.api_courses, name='api_courses'),
    path('signup/', views.signup, name='signup'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
]