from django.shortcuts import render
from .models import employee

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def skills(request):
    return render(request, 'skills.html')
def resume(request):
    return render(request, 'resume.html')
def clients(request):
    return render(request, 'clients.html')