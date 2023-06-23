# from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from .forms import (CustomUserCreationForm, CustomUserChangeForm)

# # Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
     
#     # add page
#     add_form = CustomUserCreationForm
#     add_fieldsets = (
#         ('PERSONAL INFO', {'fields': ('career', 'affiliation')}),
#         ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')})
#     )
     
#     # change page
#     form = CustomUserChangeForm
#     fieldsets = (
#         ('PERSONAL INFO', {'fields': ('career', 'affiliation')}),
#         ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )
     
#     # list page
#     list_display = ['username', 'email', 'career', 'affiliation']
 
 
# admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import (CustomUserCreationForm, CustomUserChangeForm)




# Register your models here.

# Over riding
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm    

    list_display = ('username', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = ('username',)
    ordering = ('-date_joined',)

    # admin 페이지에서 사용자 수정할때 입력폼
    fieldsets = (
        ('Personal info', {'fields': ('username','password', 'career', 'affiliation')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # admin 페이지에서 사용자 추가할때 입력폼
    add_fieldsets = (
        ('INFO', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'career', 'affiliation')
            }
        ),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # list page
    list_display = ['username', 'email', 'career', 'affiliation']

admin.site.register(CustomUser, CustomUserAdmin)