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