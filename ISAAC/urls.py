#these are our views

from django.urls import path
from .views import indexPageView, ResourcePageView, InputPageView

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('resources/', ResourcePageView, name = 'resources'),
    path('input/', InputPageView, name = 'input')
]
