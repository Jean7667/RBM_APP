from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Booking 
from django.contrib.admin.widgets import AdminTimeWidget, AdminSplitDateTime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='email')
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=254, help_text='email')
    class Meta:
        model = CustomUser
        fields = ['username', 'email','last_name']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['CustomerUser', 'checkin', 'checkout', 'location', 'notes']
