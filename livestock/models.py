from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""_summary_
    Creating a class for livestocks

    Returns:
        user: Personal in-chage of the livestock with a foireign key to the User model
        breed: The breed of the livestock
        age: The age of the livestock
        weight: The weight of the livestock
        date_created: The date the livestock
        gender: Sex of the livestock
        health_Status: The health status of the livestock        
"""
class Livestock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    health_Status = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return f"{self.breed} - {self.gender}"
    
class HealthRecord(models.Model):
    """_summary_
    creating a health record for the livestock

    Args:
        models (_type_): _description_
        

    Returns:
        livestock: The livestock the health record is for
        symptoms: The symptoms of the livestock
        diagnosis: The diagnosis of the livestock
        treatment: The treatment of the livestock
        vaccination_records: The vaccination records of the livestock
        created_at: The date the health record was created
        updated_at: The date the health record was updated
    """
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    vaccination_records = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Health Record for {self.livestock}"