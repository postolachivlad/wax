from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    path('step-01', step_one),
    path('step-02', step_two),
    path('step-03', step_three),
]
