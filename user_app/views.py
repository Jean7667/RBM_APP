from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 
    # template_name = 'base.html' start on base html 
    
""" render page
def list (request):
    return render (request,'')
"""

## access about page
def about(request):
    return render(request, 'about.html')

## sign out 
def logout(request):
    logout(request)
    return redirect('home')

def cxprofile (request):
    return render (request,'customer/customer.html')


#view for customer profile CRUD

class CxProfileView(View):
    cx_profile_template = 'cxprofile.html'

    def get(self, request):
        # find the current user
        user = request.user
            if user.is_authenticated and user.is_customer:
            return render(request, self.cx_profile_emplate, {'user': user})
        else:
            return redirect('login')