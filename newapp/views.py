from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello gaurav mishra')



# Create your views here.
