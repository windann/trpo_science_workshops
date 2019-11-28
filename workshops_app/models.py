from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse



# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название темы')
    
    def __str__(self):
        return self.name

class UserType(models.Model):
    user_type = models.CharField(max_length=30, verbose_name='Тип пользователя')

    def __str__(self):
        return self.user_type


class User(AbstractUser):
    first_name = models.TextField(verbose_name='Имя')
    last_name = models.TextField(verbose_name='Фамилия')
    avatar = models.ImageField(null=True, blank=True, upload_to='media', verbose_name='Аватарка', default='media/default.png')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True, verbose_name='Тип пользователя')

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._meta.get_field('password').verbose_name = 'Пароль'
        self._meta.get_field('username').verbose_name = 'Имя пользователя'

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

class ScienceWorkshop(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название семинара')
    description = models.CharField(max_length=500, verbose_name='Описание', default=' ')
    date_time = models.DateTimeField(verbose_name='Дата проведения')
    place = models.CharField(max_length=200, verbose_name='Место проведения')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, verbose_name='Тематика')
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Организатор')
    speaker = models.CharField(max_length=100, verbose_name='Лектор', default=None)
    is_over = models.BooleanField(null=True)
    max_listeners = models.IntegerField(null=True, verbose_name='Максимальное количество слушателей')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('science_workshop_detail_url', kwargs={'id': self.id})

    def registration_on_science_workshop(self):
        return reverse('science_workshop_registration_url', kwargs={'id': self.id})

    def update(self):
        return reverse('science_workshop_update_url', kwargs={'id': self.id})

    def archive(self):
        return reverse('science_workshop_archive_url', kwargs={'id': self.id})

    def delete(self):
        return reverse('science_workshop_delete_url', kwargs={'id': self.id})


class RegistrationOnSeminar(models.Model):
    listener = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    science_workshop = models.ForeignKey(ScienceWorkshop,on_delete=models.SET_NULL, null=True)

# class MaterialType(models.Model):
#     material_type = models.CharField(max_length=100, verbose_name='Тип', default=None)

# class Material(models.Model):
#     science_workshop = models.ForeignKey(ScienceWorkshop, on_delete=models.SET_NULL, null=True)
#     link = models.CharField(max_length=300, verbose_name='Ссылка', default=None)
#     type = models.ForeignKey(MaterialType,on_delete=models.SET_NULL, null=True)
