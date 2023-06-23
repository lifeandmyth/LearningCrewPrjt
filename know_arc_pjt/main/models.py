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



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'



class TechWorld(models.Model):
    news_date = models.CharField(max_length=20)
    news_title = models.CharField(max_length=80)
    news_text_sm = models.TextField()
    url_in = models.URLField(max_length=100)
    news_writer = models.CharField(max_length=20)
    tags_string = models.CharField(max_length=150)
    thumb_addr = models.CharField(max_length=100)
    news_site= models.CharField(max_length=20)

