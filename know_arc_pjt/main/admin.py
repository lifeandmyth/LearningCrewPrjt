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
        ('Personal info', {'fields': ('username','career','affiliation','password')}),
    )

    # admin 페이지에서 사용자 추가할때 입력폼
    add_fieldsets = (
        ('INFO', {
            'classes': ('wide',),
            'fields': ('username', 'career','affiliation','password1', 'password2')
            }
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)


# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     # add page
#     add_form = CustomUserCreationForm
#     add_fieldsets = [
#         ('INFO', {'fields': 
#                 ('username', 'email', 'career', 'affiliation')
#         }),
#     ]
     
#     # change page
#     form = CustomUserChangeForm
#     fieldsets = [
#         ('INFO', {'fields': ('username', 'email', 'career', 'affiliation')}),
#     ]
     
#     # list page
#     list_display = ['username', 'email', 'career', 'affiliation']
 
 
# admin.site.register(CustomUser, CustomUserAdmin)

#         # ('PERMISSIONS', {'fields': ['is_active', 'is_staff', 'is_superuser']}),

