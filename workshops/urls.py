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

import workshops_app.models as m

urlpatterns = [
    path('admin/', admin.site.urls),
    path('science_workshop/create', v.Service.science_workshop_create, name='science_workshop_create_url'),
    path('science_workshop/<str:id>', v.Service.science_workshop_get_detail, name='science_workshop_detail_url'),
    path('science_workshop/<str:id>/update', v.Service.science_workshop_update, name='science_workshop_update_url'),
    path('science_workshop/<str:id>/archive', v.Service.science_workshop_archive, name='science_workshop_archive_url'),
    path('science_workshop/<str:id>/delete/', v.Service.science_workshop_delete, name='science_workshop_delete_url'),
    path('science_workshop/<str:id>/registration', v.Service.science_workshop_registration, name='science_workshop_registration_url'),


    path('science_workshops/', v.Service.science_workshop_get_list, name='science_workshops'),
    path('archive', v.Service.science_workshop_get_archive_list, name='archive_url'),

    path('registration/', v.Service.user_registration, name='registration_url'),
    path('login/', v.Service.user_login, name='login'),
    path('logout/', v.Service.user_logout, name='logout'),
    path('user/<str:username>', v.Service.user_detail, name='user_detail_url'),

    

]
