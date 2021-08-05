from django.shortcuts import render
from .models import dept,emp,mul_info,ano_table,proyx_info,stu
def home(request):
    d = dept.objects.all()
    e = emp.objects.all()
    m = mul_info.objects.all()
    a = ano_table.objects.all()
    p = proyx_info.objects.all()
    s = stu.objects.all()
    return render(request,'home.html',{'dept':d,'emp':e,'mul_info':m,'ano_table':a,'proyx_info':p,'stu':s})
# Create your views here.
