"""Module for forms in the livestock app."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Livestock, HealthRecord

class SignupForm(UserCreationForm):
    """Form for user registration."""
    class Meta:
        """Meta class for the SignupForm."""
        model = User
        fields = ['username', 'password1', 'password2']# End-of-file (EOF)


class LivestockForm(forms.ModelForm):
    """Form for livestock entries."""
    class Meta:
        """Meta class for the LivestockForm."""
        model = Livestock
        fields = ['breed', 'age', 'gender', 'health_status', 'breed_image']# End-of-file (EOF)


class HealthRecordForm(forms.ModelForm):
    """Form for health records."""
    class Meta:
        """Meta class for the HealthRecordForm."""
        model = HealthRecord
        fields = ['symptoms', 'diagnosis', 'treatment', 'vaccination_records', 'livestock']# End-of-file (EOF)
