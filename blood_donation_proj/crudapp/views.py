from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm

def home(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['age']
            pw = fm.cleaned_data['blood_group']
            ge = fm.cleaned_data['gender']
            ad = fm.cleaned_data['address']
            obj = StudentModel(name=nm,age=em,blood_group=pw,gender=ge,address=ad)
            obj.save()
    else:
        fm = StudentForm()
    det = StudentModel.objects.all()
    return render(request,'home.html',{'form':fm,'details':det})
def delete(request,id):
    stu = StudentModel.objects.get(pk=id)
    stu.delete()
    return redirect('/home')
def update(request,id):
    if request.method == 'POST':
        stu = StudentModel.objects.get(pk=id)
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            messages.success(request, 'successfully updated!')
            form.save()
            return redirect('/')
    else:
        stu = StudentModel.objects.get(pk=id)
        form = StudentForm(instance=stu)
    return render(request, 'update.html', {'form': form})
def success(request):
    return render(request,'success.html')

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})

def user_login(request):
   ''' if not request.user.is_authenticated:'''
   if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
   else:
        fm = AuthenticationForm()
   return render(request, 'user_login.html', {'form': fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
