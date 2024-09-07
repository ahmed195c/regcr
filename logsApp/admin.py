from django.contrib import admin
from .models import InUseCars,RegistredCars,EmployesInfo

# Register your models here.
admin.site.register(InUseCars)
admin.site.register(RegistredCars)
admin.site.register(EmployesInfo)