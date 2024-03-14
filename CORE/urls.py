from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_app/', include('user_app.urls')),
    path('user_app/', include('django.contrib.auth.urls')), 
    path('', TemplateView.as_view(template_name='home.html'),name='home'), 
]

