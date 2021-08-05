from django.shortcuts import render
from .models import *
def home(request):
    x=man.student.all()
    return render(request,'home.html',{'man':x})
# Create your views here.
