from django import forms
#from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Booking 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.core.exceptions import ValidationError
#from django.utils import timezone
import datetime
from datetime import date

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
        fields = ['BookingExpert', 'checkin', 'checkout', 'location', 'notes']
        
        widgets = {
            'checkin': forms.DateInput(attrs={'type': 'date'}),
            'checkout': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter queryset to include only expert users
        self.fields['BookingExpert'].queryset = CustomUser.objects.filter(is_expert=True)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('BookingExpert'),
            Field('checkin', css_class='datetimepicker'),
            Field('checkout', css_class='datetimepicker'),
            Field('location'),
            Field('notes'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
                
#https://docs.djangoproject.com/en/5.0/ref/forms/validation/        
    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')
        
        # Convert checkin and checkout to datetime.date objects
        checkin_date = checkin.date() if checkin else None
        checkout_date = checkout.date() if checkout else None

        # Check if checkin date is in the past
        if checkin_date and checkin_date < date.today():
            raise ValidationError("Check-in date cannot be in the past")

        # Check if checkout date is in the past
        if checkout_date and checkout_date < date.today():
            raise ValidationError("Check-out date cannot be in the past")

        # Check if checkin date is before checkout date
        if checkin_date and checkout_date and checkin_date >= checkout_date:
            raise ValidationError("Check-in date must be before the checkout date.")

        return cleaned_data
    

class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['checkin', 'checkout', 'location', 'notes']
        widgets = {
            'checkin': forms.DateInput(attrs={'type': 'date'}),
            'checkout': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')
        
        # Convert checkin and checkout to datetime.date objects
        checkin_date = checkin.date() if checkin else None
        checkout_date = checkout.date() if checkout else None

        # Check if checkin date is in the past
        if checkin_date and checkin_date < date.today():
            raise ValidationError("Check-in date cannot be in the past")

        # Check if checkout date is in the past
        if checkout_date and checkout_date < date.today():
            raise ValidationError("Check-out date cannot be in the past")

        # Check if checkin date is before checkout date
        if checkin_date and checkout_date and checkin_date >= checkout_date:
            raise ValidationError("Check-in date must be before the checkout date.")

        return cleaned_data
    