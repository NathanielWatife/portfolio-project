"""Module for forms in the livestock app."""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    """Form for user registration."""
    class Meta:
        """Meta class for the SignupForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']# End-of-file (EOF)