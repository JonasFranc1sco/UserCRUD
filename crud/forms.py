from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Type your username'}),
            'password': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Type your password'})
        }