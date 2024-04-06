from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('list_staff', views.list_staff, name='list_staff')
]
