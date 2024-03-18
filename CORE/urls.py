from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from user_app.views import about, cxprofile, logout


    #remember that the name is the end of the url : host/user_app/signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('user_app/', include('user_app.urls')), 
    path('user_app/', include('django.contrib.auth.urls')), 
    path('user_app/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('cxprofile/', cxprofile, name='cxprofile'),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('logout/', logout, name='logout'),
   
   
]
