# Generated by Django 4.2.2 on 2023-06-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_authgroup_techworld'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmailaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254, unique=True)),
                ('verified', models.IntegerField()),
                ('primary', models.IntegerField()),
            ],
            options={
                'db_table': 'account_emailaddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountEmailconfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'account_emailconfirmation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainCustomuser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('career', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('affiliation', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'main_customuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainCustomuserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'main_customuser_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainCustomuserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'main_customuser_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTechworld',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('news_date', models.CharField(max_length=20)),
                ('news_title', models.CharField(max_length=80)),
                ('news_text_sm', models.TextField()),
                ('url_in', models.CharField(max_length=100)),
                ('news_writer', models.CharField(max_length=20)),
                ('tags_string', models.CharField(max_length=150)),
                ('thumb_addr', models.CharField(max_length=100)),
                ('news_site', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'main_techworld',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsSites',
            fields=[
                ('news_site', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('site_code', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'news_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsTechworldT',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('news_date', models.CharField(max_length=20)),
                ('news_title', models.CharField(max_length=80)),
                ('news_text_sm', models.TextField()),
                ('url_in', models.CharField(max_length=100)),
                ('news_writer', models.CharField(max_length=20)),
                ('tags_string', models.CharField(blank=True, max_length=150, null=True)),
                ('thumb_addr', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'news_techworld_t',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('uid', models.CharField(max_length=191)),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'socialaccount_socialaccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
                ('client_id', models.CharField(max_length=191)),
                ('secret', models.CharField(max_length=191)),
                ('key', models.CharField(max_length=191)),
            ],
            options={
                'db_table': 'socialaccount_socialapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialappSites',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'socialaccount_socialapp_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialtoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('token_secret', models.TextField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socialaccount_socialtoken',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TechWorld',
        ),
    ]
