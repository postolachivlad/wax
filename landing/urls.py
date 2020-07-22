from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
    path('step-01', step_one),
    path('step-02', step_two),
    path('step-03', step_three),
]
