"""Module for views in the livestock app."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Livestock, HealthRecord


# Create your views here.
def home(request):
    """View for the home page."""
    sample_livestock = Livestock.objects.all()[:3]
    return render(request, 'livestock/index.html', {'sample_livestock': sample_livestock})


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
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'livestock/login.html', {'form': form})


@login_required
def dashboard(request):
    """View for the dashboard page."""
    # Fetch livestock entries and health records associated with the current user
    livestock_entries = request.user.livestock_set.all()
    health_records = HealthRecord.objects.filter(livestock__user=request.user)
    return render(request, 'dashboard.html', {'livestock_entries': livestock_entries, 'health_records': health_records})

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
            return redirect('dashboard')
    else:
        form = LivestockForm()
    return render(request, 'add_livestock.html', {'form': form})

@login_required
def edit_livestock(request, livestock_id):
    """View for editing a livestock entry."""
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == 'POST':
        # Process form data to update the livestock entry
        form = LivestockForm(request.POST, instance=livestock)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LivestockForm(instance=livestock)
    return render(request, 'edit_livestock.html', {'form': form, 'livestock': livestock})

@login_required
def delete_livestock(request, livestock_id):
    """View for deleting a livestock entry."""
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == 'POST':
        livestock.delete()
        return redirect('dashboard')
    return render(request, 'delete_livestock.html', {'livestock': livestock})

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
            return redirect('dashboard')
    else:
        form = HealthRecordForm()
    return render(request, 'add_health_record.html', {'form': form, 'livestock': livestock})
