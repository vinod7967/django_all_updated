from django.shortcuts import render
from .forms import studentRegistration
def home(request):
    x=studentRegistration(=[fname,username])
    return render(request,'home.html',{'fm':x})
# Create your views here.
