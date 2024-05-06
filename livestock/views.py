from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *

# Create your views here.
# signup view
def signup(request):
    """_summary_
    creating a signup view

    Args:
        request (_type_): _description_
        
    Returns:
        checked request: if its a post request, it will check if the form is valid and save the user
        form: The form to be rendered
        raw_password: The raw password of the user(encrypted)
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
        
        else:
            form = AuthenticateForm()
            return render(request, 'login.html', {'form':form})



# dashboard view
@login_required
def dashboard(request):
    # get livestock entries and healthrecords associated with the currnt user
    livestock_entires = request.user.livestock_Set.all()
    health_records = HealhRecord.objets.filter(livestock__user=request.user)
    return render(request, 'dashboard.html', {'livestock_entries': livestock_entires})



# @login_required
# def add_livestock(request):
#     if request.method == 'POST':
#         # process form data to create a nwe livstock entry associating it with the current user
#         form = LivstockForm(request.POST)
#         if form.is_valid():
#             livestock = form.save(commit=False)
#             livestock.user = request.user
#             livestock.save()
#             return redirect('home')
        
#         else:
#             form = LivestockForm()
#             return render(request, 'add_livestock.html', {'form':form})
        

# @login_required
# def edith_livestock(request, livestock_id):
#     livestock = Livestock.objects.get(pk=livestock_id)
    