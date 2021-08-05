from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name','age','blood_group','gender','address']
        widgets = {
            'address': forms.TextInput(attrs={'size':'40'})
        }


