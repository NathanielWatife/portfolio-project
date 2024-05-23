"""Module for views in the livestock app."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from .models import Livestock, HealthRecord, Post
from .forms import LivestockForm, HealthRecordForm

from django.db.models import Avg




# Create your views here.
@login_required(login_url='login')
def home(request):
    """View for the home page."""
    sample_health = HealthRecord.objects.all()[:5]
    sample_livestock = Livestock.objects.all()[:5]
    return render(request, 'index.html', {
        'sample_livestock': sample_livestock,
        'sample_health': sample_health
    })


# Livestock
@login_required(login_url='login')
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
    return render(request, 'add_livestock.html', {'form': form})



# HealthRecord
@login_required(login_url='login')
def add_health_record(request, livestock_id):
    """View for adding a new health record."""
    livestock = get_object_or_404(Livestock, id=livestock_id)
    if request.method == 'POST':
        # Process form data to create a new health record for the livestock
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            health_record = form.save(commit=False)
            health_record.livestock = livestock
            health_record.save()
            return redirect('livestock_detail', livestock_id=livestock.id)
    else:
        form = HealthRecordForm()
    return render(request, 'add_health_record.html', {'form': form, 'livestock': livestock})


# retriev livestock details
def livestock_detail(request, livestock_id):
    """View for displaying the details of a specific livstock entry."""
    livestock = get_object_or_404(Livestock, id=livestock_id)
    return render(request, 'livestock_detail.html', {'livestock': livestock})

# calculate the analysis of the livestock
def livestock_analysis(request):
    """
    View for displaying the analysis of the livestock.
    """
    total_livestock = get_object_or_404(Livestock).count()
    if total_livestock > 0:
        average_age = get_object_or_404(Livestock).aggregate(Avg('age'))['age_avg']
    else:
        average_age = 0

        return render(request, 'livestock_analysis.html', {
            'total_livestock': total_livestock,
            'average_age': average_age
        })

@login_required(login_url='login')
def edit_livestock(request, livestock_id):
    """View for editing a livestock entry."""
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == 'POST':
        # Process form data to update the livestock entry
        form = LivestockForm(request.POST, instance=livestock)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LivestockForm(instance=livestock)
    return render(request, 'edit_livestock.html', {'form': form, 'livestock': livestock})

@login_required(login_url='login')
def delete_livestock(request, livestock_id):
    """View for deleting a livestock entry."""
    livestock = Livestock.objects.get(id=livestock_id)
    if request.method == 'POST':
        livestock.delete()
        return redirect('/')
    return render(request, '/', {'livestock': livestock})




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
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    """View for user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """View for user logout."""
    logout(request)
    return redirect('/login')




# Blog views
@login_required(login_url='login')
def post_list(request):
    """View for listing all posts."""
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})


@login_required(login_url='login')
def post_detail(request, year, month, day, post):
    """View for displaying a single post."""
    post = get_object_or_404(Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'detail.html', {'post': post})