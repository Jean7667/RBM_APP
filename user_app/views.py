from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import BookingForm, CustomUserCreationForm, EditBookingForm
from .models import Expert, Skill, Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages #Verified

#https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#overriding-built-in-form-templates

#Built-in Django authentication
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_customer =True 
        user.save()
        messages.success(self.request, 'Account created successfully! You can now log in.') 
        return self.render_to_response(self.get_context_data(form=form))
        #return super().form_valid(form)
   
    #in the form invalid entry 
    def form_invalid(self, form):
        messages.error(self.request, 'Account creation failed. Please check your input.')  
        return self.render_to_response(self.get_context_data(form=form))
    
    
# template_name = 'base.html' start on base html 
# Making sure the user created from the interface is idendify as a customer
# Create, but don't save the new author instance.
# new_author = f.save(commit=False)  
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/


# access about page
def about(request):
    return render(request, 'about.html')

class LogoutView(View):
     def post(self, request):
         logout(request)
         return redirect("about") #review that later

#intermediate page to logout    
def ConfirmLogout(request):
    return render (request,'registration/logout.html')
    

#view for customer profile CRUD class based view
class CxProfileView(View):
    cx_profile_template = 'customer/cxprofile.html'

    def get(self, request):
        # find the current user
        user = request.user
        if user.is_authenticated and user.is_customer:
            return render(request, self.cx_profile_template, {'user': user, 'edit_mode':True})
        else:
            return redirect('home')
         # update user data
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.first_name = request.POST.get('firstname', user.first_name)
            user.last_name = request.POST.get('lastname', user.last_name)
            user.location = request.POST.get('location', user.location)
            user.email = request.POST.get('email', user.email)
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('customer_profile')  
        else:
            messages.error(request, 'Failed to update profile. Please try again.')
            return redirect('customer_profile')
                
class DeleteCxProfileView(View):
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.delete()
            messages.success(request, 'Your profile has been deleted successfully.')
            return redirect('home')
        else:
            return redirect('unauthorized')
        

# Generic based view with skills filter (single or multiple values) to show matching list of experts


# updated view with new context object name to reflect multiple selected skills

class ExpertListView(ListView):
    model = Expert
    template_name = 'customer/listexpert.html'
    context_object_name = 'filtered_experts'
    paginate_by = 5

# defining queryset method to select multiple skills   
    def get_queryset(self):
        queryset = super().get_queryset()
        skills = self.request.GET.getlist('skills')
        #__ lookup  like using joint in SQL - 
        if skills:
            #filtering with multiple skills
            queryset = queryset.filter(skills__name__in=skills).distinct()
        # remove duplicate and make each result unique
        return queryset  
    # return data to the page unique skills and associated expert
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_skills'] = Skill.objects.all()
        return context

#############Expert list ################

""" def ExpertBooking (request):
    return render(request, 'customer/expertbooking.html') """

def expert_booking(request):
    experts = Expert.objects.all()
    return render(request, 'customer/expertbooking.html', {'experts': experts})


def expert_detail(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    return render(request, 'customer/expertdetail.html', {'expert': expert})

######## Booking Section ############
 
def booking_form(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    
        # Pre-populate the form with expert's data using the 'initial' argument
    form = BookingForm(initial={'ExpertUser': expert.user})
    
    context = {'expert': expert, 'form': form}
    return render(request, 'booking/formbooking.html', context)


@login_required
def handle_booking_submission(request, expert_id):
    expert = get_object_or_404(Expert, id=expert_id)
    
    # Check if the form is being submitted
    if request.method == 'POST':
        form = BookingForm(request.POST)  
        if form.is_valid():
            if Booking.objects.filter(CustomerUser=request.user, checkin=form.cleaned_data['checkin'], checkout=form.cleaned_data['checkout'], location=form.cleaned_data['location']).exists():
                return HttpResponse("You have already made a booking with similar details.")
            
            booking_data = form.cleaned_data
            checkin = booking_data['checkin']
            checkout = booking_data['checkout']
            location = booking_data['location']
            notes = booking_data['notes']
            
            try:
                expert_user = expert.user
                customer_user = request.user
                
                # Create a new booking
                booking = Booking.objects.create(
                    BookingExpert=expert_user,
                    CustomerUser=customer_user,
                    checkin=checkin,
                    checkout=checkout,
                    location=location,
                    notes=notes
                )
                # Redirect to the success page after booking creation
                messages.success(request, 'Booking created successfully.')
                return redirect('booking_success')
            except Exception as e:
                print("Error creating booking:", e)
                messages.error(request, "An error occurred while creating the booking.")
                return redirect('booking_form', expert_id=expert_id)
        else:
            print("Form is not valid. Errors:", form.errors)
            messages.error(request, "Form has errors. Please check the date and if the expert has been already booked.")
            return redirect('booking_form', expert_id=expert_id)
    else:
        return HttpResponseNotFound()

@login_required
def booking_success(request):
    # Retrieve bookings for the current user
    bookings = Booking.objects.filter(CustomerUser=request.user)
    
    return render(request, 'booking/bookingsuccess.html', {'bookings': bookings})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'You are going to edit the booking.')
        return redirect('booking_success')  # Redirect to booking list page
    
    return render(request, 'booking/deletebooking.html', {'booking': booking})



@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are going to edit the booking.')
            return redirect('booking_success')  # Redirect to booking detail page
    else:
        form = EditBookingForm(instance=booking)
    
    return render(request, 'booking/editbooking.html', {'form': form, 'booking': booking})    