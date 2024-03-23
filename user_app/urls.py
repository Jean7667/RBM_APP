from django.urls import path
from .views import SignUpView, CxProfileView, LogoutView, ExpertListView, DeleteCxProfileView, expert_booking, edit_booking, delete_booking, handle_booking_submission, booking_success
from . import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cxprofile/', CxProfileView.as_view(), name='customer_profile'),
    path('cxprofile/delete/', DeleteCxProfileView.as_view(), name='delete_profile'),
    path('logout/', LogoutView.as_view(), name='conf_logout'),
    path('listexpert/', ExpertListView.as_view(), name='list_expert'),
    path('expert-booking/', views.expert_booking, name='expert_booking'),
    path('expert/<int:expert_id>/', views.expert_detail, name='expert_detail'),
    path('book/<int:expert_id>/', views.booking_form, name='booking_form'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('book/<int:expert_id>/submit/', views.handle_booking_submission, name='handle_booking_submission'),
    path('booking-success/', booking_success, name='booking_success'),        
]