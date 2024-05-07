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
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_customer', 'is_expert'),
        }),
    )
    fieldsets = (
        ('Identification', {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_customer', 'is_expert')}),
    )
    
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','category','level']

class ExpertAdmin(admin.ModelAdmin):
    list_display = ['get_user_email', 'get_is_expert', 'start_date']

    def get_user_email(self, obj):
        return obj.user.email

    def get_is_expert(self, obj):
        return obj.user.is_expert

    get_user_email.short_description = 'User Email'
    get_is_expert.short_description = 'Is Expert'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Expert, ExpertAdmin)
    