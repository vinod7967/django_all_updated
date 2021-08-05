from django import forms
from .models import StudentModel
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name','age','blood_group','gender','address']
        widgets = {
            'address': forms.TextInput(attrs={'size':'40'})
        }
class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
