"""workshops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import workshops_app.views as v
import workshops_app.forms as f
import workshops_app.models as m

urlpatterns = [
    path('admin/', admin.site.urls),
    path('science_workshop/create', v.ObjectCreateService.as_view(updates = {'is_over':False,'organizer':None}, 
                                                            model_form = f.ScienceWorkshopForm,
                                                            template = 'workshop_create.html',
                                                            url = 'science_workshop_detail_url'), 
                                                            name='science_workshop_create_url'),
    path('science_workshop/<str:id>', v.ScienceWorkshopService.science_workshop_get_detail, name='science_workshop_detail_url'),
    path('science_workshop/<str:id>/update', v.ObjectUpdateService.as_view(model = m.ScienceWorkshop,
                                                                    template = 'workshop_update.html', 
                                                                    url = 'science_workshop_detail_url', 
                                                                    model_form = f.ScienceWorkshopForm), 
                                                                    name='science_workshop_update_url'),
    path('science_workshop/<str:id>/archive', v.ScienceWorkshopService.science_workshop_archive, name='science_workshop_archive_url'),
    path('science_workshop/<str:id>/delete/', v.ObjectDeleteService.as_view(model = m.ScienceWorkshop, 
                                                                    url = 'archive_url',
                                                                    template_object_name = 'science_workshop',
                                                                    template = 'workshop_delete.html'), 
                                                                    name='science_workshop_delete_url'),
    path('science_workshop/<str:id>/registration', v.ScienceWorkshopService.science_workshop_registration, name='science_workshop_registration_url'),


    path('', v.ObjectsListService.as_view(list_filters = {'is_over':False},
                                                    model = m.ScienceWorkshop, 
                                                    template = 'workshops_list.html',
                                                    list_type = 'new'), name='science_workshops'),
    path('archive/', v.ObjectsListService.as_view(list_filters = {'is_over':True},
                                            model = m.ScienceWorkshop, 
                                            template = 'workshops_list.html',
                                            list_type = 'old'), name='archive_url'),

    path('registration/', v.UserService.user_registration, name='registration_url'),
    path('login/', v.UserService.user_login, name='login'),
    path('logout/', v.UserService.user_logout, name='logout'),
    path('user/<str:id>', v.UserService.user_detail, name='user_detail_url'),

    

]
