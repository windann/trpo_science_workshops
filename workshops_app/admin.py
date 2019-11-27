from django.contrib import admin
from .models import User, UserType, ScienceWorkshop, Theme, RegistrationOnSeminar

# Register your models here.
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(ScienceWorkshop)
admin.site.register(Theme)
admin.site.register(RegistrationOnSeminar)

