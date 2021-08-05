from django import forms
class studentRegistration(forms.Form):
    username = forms.CharField(max_length=50)
    fname = forms.CharField(max_length=50)
