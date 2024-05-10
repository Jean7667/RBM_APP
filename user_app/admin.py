from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .role_service import update_user_role
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Skill, Expert, CustomUser

class CustomUserAdmin(UserAdmin):

#https://docs.djangoproject.com/en/5.0/ref/contrib/admin/ -- Override Save_model built-in Django method
    def save_model(self, request, obj, form, change):
        # Example usage: update expert status when saving CustomUser instance in admin
        update_user_role (obj, obj.is_expert, is_customer=False)
        super().save_model(request, obj, form, change)
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','first_name','last_name','is_expert','is_customer',]
    
    #create a user in 3 sections
    add_fieldsets = (
        ('Authentification', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
         ('Personal info', {
            'fields': ('first_name', 'last_name'),
        }),
         ('Role', {
            'fields': ('is_customer','is_expert'),
        }),
    )
    #edit (change user) a user in 5 sections
    fieldsets = (
        ('Identification', {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Custom Fields', {'fields': ('is_customer', 'is_expert')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

#TODO level should be a tuple review with UserStory    
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
    