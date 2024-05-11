"""Module for views in the livestock app."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Livestock
from .forms import LivestockForm, HealthRecordForm
from .models import HealthRecord



# Create your views here.
@login_required
def home(request):
    """View for the home page."""
    sample_livestock = Livestock.objects.all()[:3]
    sample_health = HealthRecord.objects.all()[:3]
    return render(request, 'livestock/index.html', {
        'sample_livestock': sample_livestock,
        'sample_health': sample_health
    })


# Livestock

@login_required
def add_livestock(request):
    """View for adding a new livestock entry."""
    if request.method == 'POST':
        # Process form data to create a new livestock entry associated with the current user
        form = LivestockForm(request.POST)
        if form.is_valid():
            livestock = form.save(commit=False)
            livestock.user = request.user
            livestock.save()
            # message.succees("")
            return redirect('/')
    else:
        form = LivestockForm()
    return render(request, 'livestock/add_livestock.html', {'form': form})



# @login_required
# def edit_livestock(request, livestock_id):
#     """View for editing a livestock entry."""
#     livestock = Livestock.objects.get(id=livestock_id)
#     if request.method == 'POST':
#         # Process form data to update the livestock entry
#         form = LivestockForm(request.POST, instance=livestock)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = LivestockForm(instance=livestock)
#     return render(request, 'livestock/edit_livestock.html', {'form': form, 'livestock': livestock})

# @login_required
# def delete_livestock(request, livestock_id):
#     """View for deleting a livestock entry."""
#     livestock = Livestock.objects.get(id=livestock_id)
#     if request.method == 'POST':
#         livestock.delete()
#         return redirect('/')
#     return render(request, '/', {'livestock': livestock})



# HealthRecord
@login_required
def add_health_record(request, livestock_id):
    """View for adding a new health record."""
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == 'POST':
        # Process form data to create a new health record for the livestock
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            health_record = form.save(commit=False)
            health_record.livestock = livestock
            health_record.save()
            return redirect('/')
    else:
        form = HealthRecordForm()
    return render(request, 'livestock/add_health_record.html', {'form': form, 'livestock': livestock})







# Authentication views
def signup(request):
    """View for user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'livestock/signup.html', {'form': form})


def login_view(request):
    """View for user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'livestock/login.html', {'form': form})


def logout_view(request):
    """View for user logout."""
    logout(request)
    return redirect('/login')