from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

def validate_min_age(value):
    if value < 18:
        raise ValidationError('Age must be 18 or older.')

class Donating(models.Model):
    groupChoices = [
        ('A+', 'A +ve'),
        ('A-', 'A -ve'),
        ('B+', 'B +ve'),
        ('B-', 'B -ve'),
        ('O+', 'O +ve'),
        ('O-', 'O -ve'),
        ('AB+', 'AB +ve'),
        ('AB-', 'AB -ve'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    donarName = models.CharField(max_length=50)
    age = models.IntegerField(validators=[validate_min_age])
    donarBloodGroup = models.CharField(max_length=3, choices=groupChoices)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    identity=models.ImageField(upload_to='donarID')