#these are our views

from django.urls import path
from .views import indexPageView, ResourcePageView, showSingleResourcePageView, updateResourcePageView, deleteResourcePageView

urlpatterns = [
    path('resources/', ResourcePageView, name = 'resources'),
    path('showresource/<int:res_id>/', showSingleResourcePageView, name = 'showSingleResource'),
    path('updateResource/', updateResourcePageView, name = 'updateRes'),
    path('deleteResource/<int:res_id>/', deleteResourcePageView, name = 'deleteResource'),
    path('', indexPageView, name = 'index'),
 
]
