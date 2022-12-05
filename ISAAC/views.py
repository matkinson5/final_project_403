from django.shortcuts import render
from .models import resources

# Create your views here.

def indexPageView(request) :
    return render(request, 'ISAAC/index.html')

def ResourcePageView(request) :
    if request.method == 'POST':

            resource = resources()

            resource.class_title = request.POST['class_title']
            resource.resource_name = request.POST['resource']
            resource.link = request.POST['link']

            resource.save()

    return render(request, 'ISAAC/resources.html')
    

def AboutPageView(request) :
    return render(request, 'ISAAC/about.html')