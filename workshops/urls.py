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
    path('science_workshop/create', v.ScienceWorkshopCreate.as_view(), name='science_workshop_create_url'),
    path('science_workshop/<str:id>', v.ScienceWorkshopDetail.as_view(), name='science_workshop_detail_url'),
    path('science_workshop/<str:id>/update', v.ScienceWorkshopUpdate.as_view(), name='science_workshop_update_url'),
    path('science_workshop/<str:id>/archive', v.archive, name='science_workshop_archive_url'),
    path('science_workshop/<str:id>/delete/', v.ScienceWorkshopDelete.as_view(), name='science_workshop_delete_url'),
    path('science_workshops/', v.science_workshops_list, name='science_workshops'),

    path('science_workshop/<str:id>/registration', v.science_workshop_registration, name='science_workshop_registration_url'),

    path('registration/', v.Registration.as_view(), name='registration_url'),
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout'),

    path('user/<str:username>', v.UserDetail.as_view(model=m.User), name='user_detail_url'),

    path('archive', v.archive_list, name='archive_url'),

]
