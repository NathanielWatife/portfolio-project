"""Modul providing URL patterns for livestock app"""
from django.urls import path
from . import views

urlpatterns = [
    # Custom url app
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add_livestock/', views.add_livestock, name='add_livestock'),
    # path('edit_livestock/<int:livestock_id>/', views.edit_livestock, name='edit_livestock'),
    # path('delete_livestock/<int:livestock_id>/', views.delete_livestock, name='delete_livestock'),
    path('livestock/<int:livestock_id>/add_health_record/', views.add_health_record, name='add_health_record'),
]# End-of-file (EOF)