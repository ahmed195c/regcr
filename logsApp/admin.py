from django.contrib import admin
from .models import InUseCars,RegistredCars,EmployesInfo,PiCarLogs

models_list = [InUseCars,RegistredCars,EmployesInfo,PiCarLogs]

for model in models_list:
    admin.site.register(model)


# Register your models here.
# admin.site.register(InUseCars)
# admin.site.register(RegistredCars)
# admin.site.register(EmployesInfo)
# admin.site.register(PiCarLogs)