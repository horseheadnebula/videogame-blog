from django import forms

from users.models import CustomUser
from .models import *

class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }