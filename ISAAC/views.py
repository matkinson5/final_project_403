from django.shortcuts import render

# Create your views here.

def indexPageView(request) :
    return render(request, 'ISAAC/index.html')

def ResourcePageView(request) :
    return render(request, 'ISAAC/resources.html')

def AboutPageView(request) :
    return render(request, 'ISAAC/about.html')