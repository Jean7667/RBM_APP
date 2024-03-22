from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Booking 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

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
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
            
            Field('CustomerUser'),
            Field('checkin', css_class='datetimepicker'),
            Field('checkout', css_class='datetimepicker'),
            Field('location'),
            Field('notes'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
