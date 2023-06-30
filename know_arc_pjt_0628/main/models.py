from django.db import models
from django.contrib.auth.models import AbstractUser
 

# Create your models here.





 # user models.py
class CustomUser(AbstractUser):
    # password = models.CharField(max_length=128)
    password = models.CharField(max_length=128, unique=False)
    username = models.CharField(unique=True, max_length=150)
    # email = models.CharField(max_length=254)
    email = models.CharField(max_length=254, unique=False, blank=True, null=True)

    CAREER = (
        ('주니어', '신입 ~ 5년차'),
        ('시니어', '5년차 이상')
    )
    KEYWORDS = (
        ('AI', 'AI'),
        ('출시', '출시'),
        ('개발', '개발'),
        ('코딩', '코딩'),
        ('클라우드', '클라우드'),
        ('공개', '공개'),
        ('서비스' ,'서비스'),
        ('언어', '언어'),
        ('프로그래밍', '프로그래밍'),
        ('기반', '기반')
    )
    career = models.CharField(verbose_name='경력', max_length=3, choices=CAREER, null=True)
    career_keyword = models.CharField(verbose_name='관심 키워드', choices=KEYWORDS, help_text = '올해의 IT키워드 10개입니다! 가장 관심 있는 항목에 체크해주세요!', max_length=100, default= None, null=True)
    affiliation = models.CharField(verbose_name='소속', max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'main_customuser'









# db models.py
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    # email = models.CharField(unique=True, max_length=254)
    email = models.CharField(max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('MainCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('MainCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class MainCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    # password = models.CharField(max_length=128)
    password = models.CharField(max_length=128, unique=False)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    # email = models.CharField(max_length=254)
    email = models.CharField(max_length=254, unique=False, blank=True, null=True)
    date_joined = models.DateTimeField(null=True)

    CAREER = (
        ('주니어', '신입 ~ 5년차'),
        ('시니어', '5년차 이상')
    )
    KEYWORDS = (
        ('AI', 'AI'),
        ('출시', '출시'),
        ('개발', '개발'),
        ('코딩', '코딩'),
        ('클라우드', '클라우드'),
        ('공개', '공개'),
        ('서비스' ,'서비스'),
        ('언어', '언어'),
        ('프로그래밍', '프로그래밍'),
        ('기반', '기반')
    )
    career = models.CharField(verbose_name='경력', max_length=3, choices=CAREER, null=True)
    career_keyword = models.CharField(verbose_name='관심 키워드', choices=KEYWORDS, help_text = '올해의 IT키워드 10개입니다! 가장 관심 있는 항목에 체크해주세요!', max_length=100, default= None, null=True)
    affiliation = models.CharField(verbose_name='소속', max_length=256, blank=True)

    class Meta:
        managed = False
        db_table = 'main_customuser'


class MainCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MainCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_customuser_groups'
        unique_together = (('customuser', 'group'),)


class MainCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MainCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)








class KeywordsBloter(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_bloter'


class KeywordsCwn(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_cwn'


class KeywordsItbiz(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_itbiz'


class KeywordsItworld(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_itworld'


class KeywordsRecentit(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_recentit'


class KeywordsTechworld(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'keywords_techworld'


class NewsSites(models.Model):
    news_site = models.CharField(primary_key=True, max_length=30)
    site_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'news_sites'


class NewsTechworldT(models.Model):
    idx = models.AutoField(primary_key=True)
    news_date = models.CharField(max_length=20)
    news_title = models.CharField(max_length=80)
    news_text_sm = models.TextField()
    url_in = models.CharField(max_length=100)
    news_writer = models.CharField(max_length=20)
    tags_string = models.CharField(max_length=150, blank=True, null=True)
    thumb_addr = models.CharField(max_length=100, blank=True, null=True)
    news_site = models.ForeignKey(NewsSites, models.DO_NOTHING, db_column='news_site')

    class Meta:
        managed = False
        db_table = 'news_techworld_t'


class RelatedKeywords(models.Model):
    words = models.CharField(max_length=50)
    related = models.CharField(max_length=158)

    class Meta:
        managed = False
        db_table = 'related_keywords'



        


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(MainCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)







class TotalKeyRelated(models.Model):
    key = models.CharField(max_length=50)
    related = models.CharField(max_length=158)

    class Meta:
        managed = False
        db_table = 'total_key_related'


class TotalTKeyrank(models.Model):
    idx = models.AutoField(primary_key=True)
    keywords = models.CharField(max_length=100)
    cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'total_t_keyrank'


class TotalTKeywordsRemake(models.Model):
    idx = models.IntegerField(primary_key=True)
    words = models.CharField(max_length=50)
    ranks = models.FloatField()

    class Meta:
        managed = False
        db_table = 'total_t_keywords_remake'


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
