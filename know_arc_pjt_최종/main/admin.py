<<<<<<< HEAD
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
from .models import CustomUser, MainCustomuser
from .forms import (CustomUserCreationForm, CustomUserChangeForm)




# Register your models here.

# Over riding
class CustomUserAdmin(UserAdmin):   
    model = CustomUser

    list_display = ('username', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username',)
    ordering = ('-date_joined',)


    # admin 페이지에서 사용자 추가할때 입력폼
    add_form = CustomUserCreationForm 
    add_fieldsets = (
        ('PERSONAL INFO', {'fields': ('username', 'password', 'career', 'career_keyword', 'affiliation')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    # admin 페이지에서 사용자 수정할때 입력폼
    form = CustomUserChangeForm
    fieldsets = (
        ('PERSONAL INFO', {'fields': ('username','password', 'career', 'career_keyword', 'affiliation')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # list page
    list_display = ['username', 'email', 'career', 'career_keyword', 'affiliation']

=======
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
 
 
>>>>>>> 63140d75cb74c4abeacb41c98c57d6d40de94777
admin.site.register(CustomUser, CustomUserAdmin)