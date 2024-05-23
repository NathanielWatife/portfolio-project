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
    path('livestock_detail/<int:livestock_id>/', views.livestock_detail, name="livestock_detail"),
    path('analysis/', views.livestock_analysis, name='analysis'),
    path('edit_livestock/<int:livestock_id>/', views.edit_livestock, name='edit_livestock'),
    path('delete_livestock/<int:livestock_id>/', views.delete_livestock, name='delete_livestock'),
    path('add_health_record/<int:livestock_id>/', views.add_health_record, name='add_health_record'),
    # Blog urls
    path('list/', views.post_list, name='list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='detail'),
]# End-of-file (EOF)