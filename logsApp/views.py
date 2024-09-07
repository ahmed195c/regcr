from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "logsApp/layout.html")


def registerCar(request):
    return render(request, "logsApp/registerCar.html")


def logsfunc(request):
    return render(request, "logsApp/logs.html")