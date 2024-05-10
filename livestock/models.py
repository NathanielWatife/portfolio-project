"""Models for the livestock app."""
from django.db import models
from django.contrib.auth.models import User

class Livestock(models.Model):
    """Model for livestock entries."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    health_status = models.CharField(max_length=200, blank=True)
    breed_image = models.ImageField(upload_to='breed_images/', blank=True)  

    def __str__(self):
        return f"{self.breed} - {self.gender}"

class HealthRecord(models.Model):
    """Model for health records."""
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    vaccination_records = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Record for {self.livestock}"
