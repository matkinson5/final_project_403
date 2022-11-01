from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return HttpResponse('Welcome to the main page')

def ResourcePageView(request) :
    return HttpResponse('Welcome to the resource database')

def InputPageView(request) :
    return HttpResponse('Welcome to the input page, where students will be putting their assignment details')