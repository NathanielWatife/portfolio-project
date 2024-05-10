"""Modul providing URL patterns for livestock app"""
from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Custom url app
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name="login"),
    path('add_livestock/', views.add_livestock, name='add_livestock'),
    path('edit_livestock/<int:livestock_id>/', views.edit_livestock, name='edit_livestock'),
    path('delete_livestock/<int:livestock_id>/', views.delete_livestock, name='delete_livestock'),
    path('add_health_record/<int:livestock_id>/', views.add_health_record, name='add_health_record'),

    # User authentication URLs
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]# End-of-file (EOF)