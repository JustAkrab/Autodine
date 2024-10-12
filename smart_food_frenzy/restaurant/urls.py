from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('check_feasible_items/', views.check_feasible_items, name='check_feasible_items'),
]