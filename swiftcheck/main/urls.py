from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('courses/', views.course, name='courses'),
    path('signup/', views.signup, name='signup'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
]