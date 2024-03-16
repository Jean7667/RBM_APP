from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Skill, Expert

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','location','name','is_manager','is_customer', 'is_expert']

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','category','level']

class ExpertAdmin(admin.ModelAdmin):
    list_display = ['user','start_date']
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Expert, ExpertAdmin)
    