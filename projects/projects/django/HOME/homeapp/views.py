from django.shortcuts import render
def homepage(request):
    return render(request,'result.html')
def login(request):
    return render(request,'lodinpage.html')
def signup(request):
    return render(request,'signuppage.html')




# Create your views here.
