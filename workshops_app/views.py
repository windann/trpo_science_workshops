from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import ScienceWorkshop, UserType, User, RegistrationOnSeminar
from .forms import ScienceWorkshopForm, RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

class DataMapper():
    def get_object(model_object,id):
        return get_object_or_404(model_object, id__iexact=id)

    def filter_objects(model_object,filters):
        return model_object.objects.filter(**filters)

    def update_object(model_object, updates):
        for k, v in updates.items():
            setattr(model_object, k, v)
        return model_object

    def save_object(model_object):
        model_object.save()
        return model_object

    def delete_object(model_object):
        model_object.delete()
        return model_object

class ObjectDeleteService(View):
    model = None
    url = None
    template_object_name = None
    template = None

    def get(self,request, id):
        object = DataMapper.filter_objects(self.model, {'id':id})
        return render(request, self.template, context={self.template_object_name: object})

    def post(self,request, id):
        object = DataMapper.filter_objects(self.model, {'id':id})
        DataMapper.delete_object(object)
        return redirect(self.url)

class ObjectUpdateService(View):
    model = None
    url = None
    template = None
    model_form = None

    def get(self, request, id):
        object = DataMapper.get_object(self.model, id)
        form = self.model_form(instance = object)
        return render(request, self.template, context={'form': form})

    def post(self, request, id):
        object = DataMapper.get_object(self.model, id)
        form = self.model_form(request.POST, instance=object)

        if form.is_valid():
            changed_object = form.save()
            return redirect(self.url, id=changed_object.id)

        return render(request, self.template, context={'form': form})

class ObjectsListService(View):
    list_filters = None
    model = None
    template = None 
    list_type = None

    def get(self, request):
        objects = DataMapper.filter_objects(self.model, self.list_filters)
        return render(request, self.template, context={'science_workshops': objects, 'list_type': self.list_type})

class ObjectCreateService(View):
    updates = {'is_over':False,'organizer':None}
    model_form = None 
    template = None 
    url = None 

    def get(self,request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self,request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_object = bound_form.save()
            DataMapper.save_object(new_object)
            if self.updates:
                self.updates['organizer'] = request.user
                DataMapper.update_object(new_object, self.updates)
                DataMapper.save_object(new_object)
            return redirect(self.url, id=new_object.id)

        return render(request, self.template, context={'form': bound_form})

class ScienceWorkshopService(View):

    def science_workshop_archive(request, id):
        science_workshop = DataMapper.get_object(ScienceWorkshop, id)
        DataMapper.update_object(science_workshop, {'is_over':True})
        DataMapper.save_object(science_workshop)
        return redirect('science_workshops')


    def science_workshop_get_detail(request, id):
        model = ScienceWorkshop
        template = 'workshop_detail.html'

        if request.method == 'GET':
            science_workshop = DataMapper.get_object(model, id)
            registrations = len(DataMapper.filter_objects(RegistrationOnSeminar, {'science_workshop':science_workshop}))
            left = science_workshop.max_listeners - registrations
            if request.user.is_authenticated:
                is_registrated = len(DataMapper.filter_objects(RegistrationOnSeminar, {'listener':request.user, 'science_workshop':science_workshop}))
            else:
                is_registrated = 1
            return render(request, template, context={'science_workshop': science_workshop, 
                                                            'registrations':registrations, 
                                                            'left': left,
                                                            'is_registrated': is_registrated
                                                            })

    @login_required
    def science_workshop_registration(request, id):
        user = request.user
        science_workshop = DataMapper.get_object(ScienceWorkshop, id__iexact=id)
        user_registration = DataMapper.filter_objects(RegistrationOnSeminar,{'listener':user, 'science_workshop':science_workshop})
        if user_registration:
            return redirect('science_workshop_detail_url', id=science_workshop.id)
        else:
            registration = RegistrationOnSeminar(listener=user, science_workshop=science_workshop)
            DataMapper.save_object(registration)

            return redirect('science_workshops')

class UserService(View):

    def user_detail(request, username):
        if request.method == 'GET':
            user = DataMapper.get_object(User, id)
            return render(request, 'user_detail.html', context={'user_p': user})


    def user_registration(request):
        if request.method == 'GET':
            form = RegistrationForm()
            template = 'registration.html'
            context = {'form': form}

            return render(request, template, context)

        else:
            form = RegistrationForm(request.POST,request.FILES, instance=User())

            if form.is_valid():
                new_user = form.save()
                DataMapper.save_object(new_user)
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('user_detail_url', id=new_user.id)

            context = {'form': form}

            return render(request, 'registration.html', context)


    @login_required
    def user_logout(request):
        logout(request)
        return redirect('science_workshops')


    def user_login(request):

        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('science_workshops')
        else:
            form = AuthenticationForm(request)
        return render(request, 'login.html', {'form': form})