from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='email')
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=254, help_text='email')
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

