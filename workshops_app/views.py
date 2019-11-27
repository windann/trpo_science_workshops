from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import ScienceWorkshop, UserType, User, RegistrationOnSeminar
from .forms import ScienceWorkshopForm, RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

class ScienceWorkshopDetail(View):
    model = ScienceWorkshop
    template = 'workshop_detail.html'

    def get(self, request, id):
        science_workshop = get_object_or_404(self.model, id__iexact=id)
        registrations = len(RegistrationOnSeminar.objects.filter(science_workshop=science_workshop))
        left = science_workshop.max_listeners - registrations
        if request.user.is_authenticated:
            is_registrated = len(RegistrationOnSeminar.objects.filter(listener = request.user, science_workshop=science_workshop))
        else:
            is_registrated = 1
        return render(request, self.template, context={'science_workshop': science_workshop, 
                                                        'registrations':registrations, 
                                                        'left': left,
                                                        'is_registrated': is_registrated
                                                        })

def science_workshops_list(request):
    science_workshops = ScienceWorkshop.objects.filter(is_over=False)
    return render(request, 'workshops_list.html', context={'science_workshops': science_workshops, 'list_type': 'new'})

def archive_list(request):
    science_workshops = ScienceWorkshop.objects.filter(is_over=True)
    return render(request, 'workshops_list.html', context={'science_workshops': science_workshops, 'list_type': 'archive'})

def archive(request, id):
    science_workshop = get_object_or_404(ScienceWorkshop, id__iexact=id)
    science_workshop.is_over = True
    science_workshop.save()
    return redirect('science_workshops')


class ScienceWorkshopCreate(View):
    def get(self, request):
        form = ScienceWorkshopForm()
        return render(request, 'workshop_create.html', context={'form': form})

    def post(self, request):
        bound_form = ScienceWorkshopForm(request.POST)

        if bound_form.is_valid():
            new_science_workshop = bound_form.save()
            new_science_workshop.save()
            new_science_workshop.is_over = False
            new_science_workshop.organizer = request.user
            new_science_workshop.save()
            return redirect('science_workshop_detail_url', id=new_science_workshop.id)

        return render(request, 'workshop_create.html', context={'form': bound_form})

class ScienceWorkshopUpdate(View):
    def get(self, request, id):
        science_workshop = get_object_or_404(ScienceWorkshop, id__iexact=id)
        form = ScienceWorkshopForm(instance=science_workshop)
        return render(request, 'workshop_update.html', context={'form': form})

    def post(self, request, id):
        science_workshop = get_object_or_404(ScienceWorkshop, id__iexact=id)
        form = ScienceWorkshopForm(request.POST, instance=science_workshop)

        if form.is_valid():
            changed_science_workshop = form.save()
            return redirect('science_workshop_detail_url', id=changed_science_workshop.id)

        return render(request, 'workshop_update.html', context={'form': form})

class ScienceWorkshopDelete(View):
    def get(self, request, id):
        science_workshop = ScienceWorkshop.objects.get(id__iexact=id)
        print('туть')
        return render(request, 'workshop_delete.html', context={'science_workshop': science_workshop})

    def post(self, request, id):
        science_workshop = ScienceWorkshop.objects.filter(id=id)
        science_workshop.delete()
        return redirect('archive_url')

@login_required
def science_workshop_registration(request, id):
    user = request.user
    science_workshop = get_object_or_404(ScienceWorkshop, id__iexact=id)

    user_registration = RegistrationOnSeminar.objects.filter(listener=user, science_workshop=science_workshop)

    if user_registration:
        return redirect('science_workshop_detail_url', id=science_workshop.id)
    else:
        registration = RegistrationOnSeminar(listener=user, science_workshop=science_workshop)
        registration.save()

        return redirect('science_workshops')

@login_required
def logout_view(request):
    logout(request)
    return redirect('science_workshops')


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('science_workshops')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        template = 'registration.html'
        context = {'form': form}

        return render(request, template, context)

    def post(self, request):
        form = RegistrationForm(request.POST,request.FILES, instance=User())

        if form.is_valid():
            new_user = form.save()
            new_user.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('user_detail_url', username=new_user.username)

        context = {'form': form}

        return render(request, 'registration.html', context)

class UserDetail(View):
    model = None
    template = 'user_detail.html'

    def get(self, request, username):
        user = get_object_or_404(self.model, username__iexact=username)
        return render(request, self.template, context={'user_p': user})