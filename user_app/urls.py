from django.urls import path
from .views import SignUpView, CxProfileView, LogoutView, ExpertListView, DeleteCxProfileView, expert_booking
from . import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cxprofile/', CxProfileView.as_view(), name='customer_profile'),
    path('cxprofile/delete/', DeleteCxProfileView.as_view(), name='delete_profile'),
    path('logout/', LogoutView.as_view(), name='conf_logout'),
    path('listexpert/', ExpertListView.as_view(), name='list_expert'),
    path('expert-booking/', views.expert_booking, name='expert_booking'),
    path('expert/<int:expert_id>/', views.expert_detail, name='expert_detail'),        
]