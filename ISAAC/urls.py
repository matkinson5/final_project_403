#these are our views

from django.urls import path
from .views import indexPageView, ResourcePageView, AboutPageView

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('resources/', ResourcePageView, name = 'resources'),
    path('about/', AboutPageView, name = 'about'),
]
