from django.shortcuts import render
from django.shortcuts import redirect


from django.views.generic import View

def index(request):
  return render(request, "landing/index.html", {})

def step_one(request):
  return render(request, "landing/step1.html", {})

def step_two(request):
  return render(request, "landing/step2.html", {})

def step_three(request):
  return render(request, "landing/step3.html", {})
