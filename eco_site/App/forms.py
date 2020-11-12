from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    Email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        labels={'email':'Email'}
