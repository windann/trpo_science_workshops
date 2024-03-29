# Generated by Django 2.2.7 on 2019-11-26 16:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.TextField(verbose_name='Имя')),
                ('last_name', models.TextField(verbose_name='Фамилия')),
                ('avatar', models.ImageField(blank=True, default='media/default.png', null=True, upload_to='media', verbose_name='Аватарка')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название темы')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=30, verbose_name='Тип пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='ScienceWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название семинара')),
                ('date_time', models.DateTimeField(verbose_name='Дата проведения семинара')),
                ('place', models.CharField(max_length=200, verbose_name='Место проведения семинара')),
                ('is_over', models.BooleanField(null=True)),
                ('listener', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='listener_set', to=settings.AUTH_USER_MODEL, verbose_name='Слушатель')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer_set', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshops_app.Theme', verbose_name='Тематика')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workshops_app.UserType', verbose_name='Тип пользвателя'),
        ),
    ]
