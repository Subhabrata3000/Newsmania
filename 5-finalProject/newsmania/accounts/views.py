from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')
    # return HttpResponse("This is Login page")

def register(request):
    return render(request, 'register.html')
    # return HttpResponse("This is register page")
