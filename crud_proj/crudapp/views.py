from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel
from django.contrib import messages
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
    return redirect('/')
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

