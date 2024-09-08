from django.shortcuts import render
from django import forms
from logsApp.models import InUseCars , RegistredCars , EmployesInfo
# Create your views here.


def index(request):
    return render(request, "logsApp/layout.html")


def registerCar(request):
    if request.method == "POST":
        ceoN = request.POST["ceoNumber"]
        carnumberreq = request.POST.get("carNumber")  # Use .get() to avoid KeyError if carNumber is not in POST
        allregscars = RegistredCars.objects.all()
        employe = EmployesInfo.objects.get(ceoNumber=ceoN)

        if carnumberreq:
            try:
                car = RegistredCars.objects.get(carNumber=carnumberreq)
                # If a car with this number exists, you can work with 'car'
                newInuseCar = InUseCars(ceoNumber=ceoN,
                                        carNumber=carnumberreq,
                                        instance=employe)
                newInuseCar.save()
                print("Car found")
                return render(request,"logsApp/registerCar.html",{"car":car, "em":employe})
                # Do something with 'car'
            except RegistredCars.DoesNotExist:
                # Handle the case where the car number doesn't exist
                print("Car not found")

        return render(request, "logsApp/registerCar.html",{"all":allregscars})
    
    return render(request, "logsApp/registerCar.html",)


def logsfunc(request):
    return render(request, "logsApp/logs.html")