from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CAREER = (
        ('주니어', '신입 ~ 5년차'),
        ('시니어', '5년차 이상')
    )
    career = models.CharField(verbose_name='경력', max_length=3, choices=CAREER, unique=True, null=True)
    affiliation = models.CharField(verbose_name='소속', max_length=256, blank=True)

class NewsSites(models.Model):
    news_site = models.CharField(primary_key=True, max_length=30)
    site_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'news_sites'

class TotalnewsKT(models.Model):
    idx = models.IntegerField(primary_key=True)
    news_date = models.DateTimeField()
    news_title = models.CharField(max_length=124)
    news_text_sm = models.TextField()
    url_in = models.CharField(max_length=128)
    news_writer = models.CharField(max_length=50)
    tags_string = models.CharField(max_length=188, blank=True, null=True)
    thumb_addr = models.CharField(max_length=228, blank=True, null=True)
    news_site = models.ForeignKey(NewsSites, on_delete=models.DO_NOTHING, db_column='news_site')
    total_keywords = models.CharField(max_length=188)

    class Meta:
        managed = False
        db_table = 'totalnews_k_t'
