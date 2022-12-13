from django.shortcuts import render
from .models import resources

#home page and record input 
def indexPageView(request) :
    if request.method == 'POST':

        resource = resources()

        resource.class_title = request.POST['class_title']
        resource.resource_name = request.POST['resource']
        resource.link = request.POST['link']

        resource.save()

        data = resources.objects.all()

        context = {
            "res" : data
        }

        return render(request, 'ISAAC/resources.html', context)

    else: 
        return render(request,'ISAAC/index.html' ) 

#display resources
def ResourcePageView(request) :
    data = resources.objects.all()

    context = {
        "res" : data
    }
    return render(request, 'ISAAC/resources.html', context)

#get info from record to edit
def showSingleResourcePageView(request, res_id) :
    data = resources.objects.get(id = res_id)

    context = {
        "record" : data
    }

    return render(request, 'ISAAC/edit.html', context)

#update exsisting record
def updateResourcePageView(request) :
    if request.method == 'POST' :
        res_id = request.POST['res_id']

        resource = resources.objects.get(id = res_id)

        resource.class_title = request.POST['class_title']
        resource.resource_name = request.POST['resource']
        resource.link = request.POST['link']

        resource.save()
    return ResourcePageView(request)

#delete record
def deleteResourcePageView(request, res_id) :
    data = resources.objects.get(id=res_id)
    
    data.delete()

    return ResourcePageView(request)