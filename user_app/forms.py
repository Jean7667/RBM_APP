from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = CustomUser
            fields = UserCreationForm.Meta.fields # ('add the field you want to show in the login page','')
        
class CustomUserChangeForm(UserChangeForm):
        class Meta:
            model = CustomUser
            fields = UserChangeForm.Meta.fields
            
            
