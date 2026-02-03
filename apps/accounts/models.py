from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    salutation = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])
    phone = models.CharField(
        max_length=20, 
        blank=True,
        validators=[
            RegexValidator(r'^\+?\d{7,15}$', 'Enter a valid phone number.')
        ]
    )
    affiliation = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)

    is_author = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    def has_role(self, role_name):
        return self.groups.filter(name=role_name).exists()