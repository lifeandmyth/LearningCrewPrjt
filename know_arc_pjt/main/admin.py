from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import (CustomUserCreationForm, CustomUserChangeForm)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
     
    # add page
    add_form = CustomUserCreationForm
    add_fieldsets = (
        ('NAME', {'fields': ('first_name', 'last_name')}),
        ('PERSONAL INFO', {'fields': ('career', 'affiliation')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
     
    # change page
    form = CustomUserChangeForm
    fieldsets = (
        ('NAME', {'fields': ('first_name', 'last_name')}),
        ('PERSONAL INFO', {'fields': ('career', 'affiliation')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
     
    # list page
    list_display = ['username', 'email', 'career', 'affiliation']
 
 
admin.site.register(CustomUser, CustomUserAdmin)