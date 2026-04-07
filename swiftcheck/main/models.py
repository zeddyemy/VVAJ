from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    class Courses(models.TextChoices):
        FRONTEND = 'FRONTEND', 'Frontend Development'
        BACKEND = 'BACKEND', 'Backend Development'


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=User.Courses.choices)
    
    
    
    
    
    
    
    