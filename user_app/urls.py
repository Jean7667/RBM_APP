from django.urls import include, path
from .views import SignUpView
from .views import CxProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cxprofile/', CxProfileView.as_view(), name='customer_profile'),
    path('cxprofile/delete/', CxProfileView.as_view(), name='delete_profile'),
]