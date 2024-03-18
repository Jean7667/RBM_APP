from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Skill, Expert

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','first_name','last_name','is_expert','is_customer',]
    add_fieldsets = (
        (None, {
            'classes': ('wide','extrapretty'),
            'fields': ('username', 'email', 'password1', 'password2',),
        }),
    )
    
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','category','level']


class ExpertAdmin(admin.ModelAdmin):
    list_display = ['user','start_date',]
 
#todo MISSING FIELDS IN ADMIN INTERFACE TIME CONSUMMING PROBLEM



























    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Expert, ExpertAdmin)
    