from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fruits


# Create your views here.

def index(request):
    return HttpResponse("hello")







