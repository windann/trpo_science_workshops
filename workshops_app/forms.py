from django import forms
from .models import ScienceWorkshop, User
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


class ScienceWorkshopForm(forms.ModelForm):
    class Meta:
        model = ScienceWorkshop
        fields = ['title','theme', 'speaker', 'date_time', 'place', 'description','max_listeners', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time': forms.DateInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'max_listeners': forms.TextInput(attrs={'class': 'form-control'}),
            'speaker': forms.TextInput(attrs={'class': 'form-control'})
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'user_type']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'password2': 'Пароль',
        }