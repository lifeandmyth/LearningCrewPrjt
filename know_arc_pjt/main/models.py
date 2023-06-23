from django.db import models
from django.contrib.auth.models import AbstractUser
 

# Create your models here.
 
class CustomUser(AbstractUser):

    # 추가 필드 (career, affiliation)
     
    CAREER = (
        ('주니어', '신입 ~ 5년차'),
        ('시니어', '5년차 이상')
    )
    career = models.CharField(verbose_name='경력', max_length=3, choices=CAREER, unique=True, null=True)
    affiliation = models.CharField(verbose_name='소속', max_length=256, blank=True)
    
    # # Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
     
#     # add page
#     add_form = CustomUserCreationForm
#     add_fieldsets = [
#         ('NAME', {'fields': ['first_name', 'last_name']}),
#         ('PERSONAL INFO', {'fields': ['career', 'affiliation']}),
#         ('PERMISSIONS', {'fields': ['is_active', 'is_staff', 'is_superuser']})
#     ]
     
#     # # change page
#     # form = CustomUserChangeForm
#     # fieldsets = [
#     #     ('NAME', {'fields': ['first_name', 'last_name']}),
#     #     ('PERSONAL INFO', {'fields': ['career', 'affiliation']}),
#     #     ('PERMISSIONS', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
#     # ]
     
#     # list page
#     list_display = ['username', 'email', 'career', 'affiliation']
 
 
# admin.site.register(CustomUser, CustomUserAdmin)

