from django.shortcuts import render
from app1.models import *

# Create your views here.
def student(request):
    data1=Student.objects.all()
    return render(request,'student.html',{'data1':data1})

def index(request):
    data2=Index.objects.all()
    return render(request,'index.html',{'data2':data2})

def about(request):
    data3=About.objects.all()
    return render(request,'about.html',{'data3':data3})